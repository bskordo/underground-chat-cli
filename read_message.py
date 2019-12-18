import asyncio
import logging
from aiofile import AIOFile
import datetime
from utils import get_connection
from contextlib import asynccontextmanager
import configargparse


def get_cli_args():
    parser = configargparse.ArgumentParser()
    parser.add('--server', required=True,
               help='a server to connect to chat', env_var='SERVER_PATH')
    parser.add('--reading_port', required=True,
               help='a server to connect to chat', env_var='READING_PORT')
    return parser.parse_args()


async def write_msg_into_file(received_msg):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d-%H.%M")
    chat_msg = received_msg.decode()
    msg_with_data = '[{}]: {}'.format(current_time, chat_msg)
    async with AIOFile("history_msg.txt", 'a') as file_for_writing:
                await file_for_writing.write(msg_with_data)


async def read_msg():
    command_line_args = get_cli_args()
    while True:
        reader, _ = await get_connection(command_line_args.server,
                                         command_line_args.reading_port)
        received_msg = await reader.readline()
        await write_msg_into_file(received_msg)
        print(received_msg.decode().strip())


def main():
    asyncio.run(read_msg())


if __name__ == '__main__':
    main()
