import math
import time
import requests
import pandas as pd
from datetime import datetime
from dotenv import dotenv_values
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

BASE_URL = "https://logbook.qrz.com/api"


def parse_freq(f): # noqa C901
    fbase = int(math.floor(f))
    if fbase == 1:
        return "160m"
    elif fbase == 3 or fbase == 4:
        return "80m"
    elif fbase == 5:
        return "60m"
    elif fbase == 7:
        return "40m"
    elif fbase == 10:
        return "30m"
    elif fbase == 14:
        return "20m"
    elif fbase == 18:
        return "17m"
    elif fbase == 21:
        return "15m"
    elif fbase == 24:
        return "12m"
    elif fbase == 28 or fbase == 29:
        return "10m"
    elif fbase >= 50 and fbase <= 54:
        return "6m"
    elif fbase >= 144 and fbase <= 148:
        return "2m"
    else:
        return None


def get_qsos() -> pd.DataFrame:
    return pd.read_csv(
        env["LOG_PATH"],
        names=[
            "date_start",
            "time_start",
            "date_end",
            "time_end",
            "call",
            "square",
            "frequency",
            "qso_mode",
            "sent",
            "received",
            "power",
            "unk0",
            "unk1",
            "unk2",
        ],
    )


def build_req_adif_str(data):
    # http://adif.org.uk/312/ADIF_312.htm#Data_Types_Enumerations_and_Fields
    if data.band is None:
        return None

    d = datetime.strptime(f"{data.date_end} {data.time_end}", "%Y-%m-%d %H:%M:%S")
    qso_date = d.strftime("%Y%m%d")
    qso_time = d.strftime("%H%M")

    return f"<band:{len(data.band)}>{data.band}\
        <mode:{len(data.qso_mode)}>{data.qso_mode}\
        <call:{len(data.call)}>{data.call}\
        <qso_date:{len(qso_date)}>{qso_date}\
        <station_callsign:{len(env['MY_CALL'])}>{env['MY_CALL']}\
        <time_on:{len(qso_time)}>{qso_time}\
        <tx_pwr:{len(str(data.power))}>{str(data.power)}\
        <freq:{len(str(data.frequency))}>{str(data.frequency)}\
        <eor>".replace(
        " ", ""
    )


class WsjtxLogHandler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        if event.is_directory or event.event_type == 'created':
            return None
        elif event.event_type == 'modified' and \
                env['LOG_PATH'].split('/')[-1] in event.src_path:
            qso = get_qsos().iloc[-1]
            qso['band'] = parse_freq(qso.frequency)

            resp = requests.post(
                BASE_URL,
                data={
                    "KEY": env["USR_KEY"],
                    "ACTION": "INSERT",
                    "ADIF": build_req_adif_str(qso)},
            )

            print(resp.text)


if __name__ == "__main__":
    env = dotenv_values(".env")

    wsjtx_logbook_observer = Observer()
    log_handler = WsjtxLogHandler()

    wsjtx_logbook_observer.schedule(
        log_handler,
        '/'.join(env['LOG_PATH'].split('/')[:-1]),
        recursive=True)

    wsjtx_logbook_observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        wsjtx_logbook_observer.stop()
        wsjtx_logbook_observer.join()
