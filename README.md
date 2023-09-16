# QRZ Pal
A Logbook helper to automatically forward your wsjt-x QSOs to QRZ. For Free (requires QRZ XML Data subscription)! Most of the testing has been on OSX but it should translate to Linux as well.

## Development Setup/Install
- Setup virtualenv in which to install the scripts dependencies
```shell
python3 -m venv qrzpal_env
source qrzpal_env/bin/activate
python3 -m pip install poetry
poetry install
```
## Configuration
- Setup environment variables:
  - create a file in the cloned directory named `.env`, place the following key value pairs inside and save it. The `USR_KEY` for your QRZ account can be accessed here: https://www.qrz.com/docs/logbook30/api
  - the `LOG_PATH` on OSX is `/Users/<username>/Library/Application Support/WSJT-X/wsjtx.log`
```
USR_KEY=your_qrz_usr_key_here
LOG_PATH=your_wsjt-x_.log_file_path_here
MY_CALL=your_callsign_here
```

## How to Use It
Before starting a session in wsjt-x, run the following commands in a terminal window
```shell
source qrzpal_env/bin/activate # if not already activated, steps to create and install dependencies above
python3 -m qrzpal
```
Continue on to using wsjt-x as usual. After finishing your wsjt-x session, kill the qrzpal process with CTRL+C
## Open Items:
- [ ] Reference `wsjtx_log.adi` instead of `wsjtx.log` this will greatly simplify/eliminate parsing required ahead of the request to QRZ
- [ ] Build and publish wheel for easier package consumption

73 DE N8ACD

