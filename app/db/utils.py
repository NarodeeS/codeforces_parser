import time

from .base import engine 


def wait_unlesss_db_started() -> None:
    connected = False
    while not connected:
        if database_started():
            connected = True
            
        time.sleep(1)


def database_started() -> bool:
    try:
        engine.connect()
        return True
    except Exception as e:
        print(e)
        return False
