# Chat-cli

A service which allow read and send msg from chat server,


## How to set up

For run the scripts need to use Python version upper than 3.7
Need to also set as env variable server address ,port and token

```bash
export SERVER_PATH='server address'
export READING_PORT='port'
export TOKEN='user token'
export WRITING_PORT='port'
```

## How to run

```bash
python read_message.py
python send_message.py --msg 'user_msg' --user_name 'user_name'
```
