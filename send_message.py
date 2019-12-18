import asyncio
import time
import logging
import json
from utils import get_connection
import configargparse
import os
from os import environ


def get_cli_args():
    parser = configargparse.ArgumentParser()
    parser.add('--server', required=True, help='a server to connect to chat',
               env_var='SERVER_PATH')
    parser.add('--port', required=True, help='a port to connect to chat',
               env_var='WRITING_PORT')
    parser.add('--msg', help='msg to send to chat')
    parser.add('--token', required=True, help='a server to connect to chat',
               env_var='TOKEN')
    parser.add('--user_name')
    return parser.parse_args()


async def authenticate_user(user_hash, reader, writer):
    info_message = await reader.readline()
    writer.write((user_hash+('\n')).encode())
    info_message = await reader.readline()
    if json.loads(info_message.decode()):
        return True
    else:
        return False


async def register_user(reader, writer, user_name=None):
    writer.write(('\n').encode())
    register_message = await reader.readline()
    logging.info(f'register_message: {register_message.strip()}')
    if user_name:
        writer.write(user_name.encode())
    else:
        writer.write('\n'.encode())
    user_credentials = await reader.readline()
    logging.info(f'user_credentials: {user_credentials.strip()}')
    return json.loads(user_credentials.decode())['account_hash']


async def submit_msg(msg, reader, writer):
    writer.write(('\n').encode())
    sended_message = await reader.readline()
    if msg:
        writer.write((msg+('\n\n')).encode())
    else:
        writer.write(('\n\n').encode())
    sended_message = await reader.readline()
    logging.info(f'Sended_message: {sended_message.strip()}')


async def send_user_msg():
    command_line_args = get_cli_args()
    reader, writer = await get_connection(server=command_line_args.server,
                                          port=command_line_args.port)
    if await authenticate_user(command_line_args.token, reader, writer):
        await submit_msg(command_line_args.msg, reader, writer)
    else:
        user_hash = await register_user(reader, writer,
                                        command_line_args.user_name)
        os.environ['TOKEN'] = user_hash
        print('Your token was wrong,please run the script one more time')


def main():
    asyncio.run(send_user_msg())


if __name__ == '__main__':
    main()
