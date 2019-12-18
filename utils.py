import asyncio
import time
import logging
from aiofile import AIOFile
import datetime
from contextlib import asynccontextmanager

COUNT_OF_ATTEMP = 2
SLEEPING_TIME = 5


@asynccontextmanager
async def open_connection(server, port):
    connection_attempt = 0
    reader = None
    while reader is None:
        try:
            reader, writer = await asyncio.open_connection(server, port)
        except (ConnectionResetError, ConnectionError, OSError):
            if connection_attempt < COUNT_OF_ATTEMP:
                time.sleep(SLEEPING_TIME)
                connection_attempt += 1
            else:
                error_msg = 'Нет соединения. Повторная попытка.'
                logging.debug(error_msg)
                async with AIOFile("history_msg.txt", 'a') as file_for_writing:
                    await afp.write(file_for_writing)
    yield reader, writer


async def get_connection(server, port):
    async with open_connection(server, port) as connection:
        return connection
