# Chat-cli

A service which has been implemented by async python.  It allows to read and send msg from chat server.


## How to set up

For run the scripts need to use Python version upper than 3.7.
Need to also set as env variable server address ,port and token. You can easily find description of parametrs bu put '--help'
for example:
```bash
python send_message.py --help
usage: send_message.py [-h] --server SERVER --port PORT [--msg MSG] --token
                       TOKEN [--user_name USER_NAME]

If an arg is specified in more than one place, then commandline values
override environment variables which override defaults.

optional arguments:
  -h, --help            show this help message and exit
  --server SERVER       a server to connect to chat [env var: SERVER_PATH]
  --port PORT           a port to connect to chat [env var: WRITING_PORT]
  --msg MSG             msg to send to chat
```
### Set up enviroment variables
```bash
export SERVER_PATH='server address'
export READING_PORT='port'
export TOKEN='user token'
export WRITING_PORT='port'
```

## How to run the scripts and sample output

```bash
python send_message.py --msg 'Hello'
python read_message.py
Eva: Поэтому ты ошибаешься.
Vlad: Прекрати это.
Eva: ОК, пока.
Hopeful : Hello
```