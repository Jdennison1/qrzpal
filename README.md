# QRZ Pal
A Logbook helper to automatically forward your wsjt-x QSOs to QRZ. For Free (requires QRZ XML Data subscription)!

## Setup
- Setup virtualenv in which to install the scripts dependencies
```shell
python3 -m venv qrzpal_env
source qrzpal_env/bin/activate
python3 -m pip install poetry
poetry install
```
- Setup environment variables:
  - create a file in the cloned directory named `.env`, place the following key value pairs inside and save it. The `USR_KEY` for your QRZ account can be accessed here: https://www.qrz.com/docs/logbook30/api
```
USR_KEY=your_qrz_usr_key_here
LOG_PATH=your_wsjt-x_.log_file_path_here
MY_CALL=your_callsign_here
```

## Use
Before starting a session in wsjt-x, run the following commands
```shell
source qrzpal_env/bin/activate # if not already activated
python3 -m qrzpal
```
Continue on to using wsjt-x as usual. After finishing your wsjt-x session, kill the qrzpal process with CTRL+C

