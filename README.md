# QRZ Pal

## Setup
- Setup virtualenv in which to install the scripts dependencies
```shell
python3 -m venv qrzpal_env
source qrzpal_env/bin/activate
python3 -m pip install -r requirements.txt
```
- Setup environment variables:
  - create a file in the cloned directory named `.env`, place the following key value pairs inside and save it. The `USR_KEY` for your QRZ account can be accessed here: https://www.qrz.com/docs/logbook30/api
```
USR_KEY=your_qrz_usr_key_here
LOG_PATH=your_wsjt-x_.log_file_path_here
MY_CALL=your_callsign_here
```

## Use
Once you finish a session in wsjt-x, run the following command
```shell
python3 ./qrpal.py
```
When the script completes, navigate to your wsjt-x .log file (the one referenced in your .env file) and clear out the contents and save the file. This will prevent the qrzpal script from attempting duplicate logbook inserts for future sessions.

