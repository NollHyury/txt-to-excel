import os
from datetime import datetime
from pathlib import Path


def file_exists(file_path : str) -> bool:
    returnValue = False
    try:
        f = open(file_path)
        f.close()
        returnValue = True
    except IOError as io_error:
        print(io_error)
        returnValue = False
    finally:
        return returnValue


def file_is_updated(file_path : str) -> bool:
    if file_exists(file_path):
        fmt = '%d-%m-%Y'
        dateNow = datetime.today().strftime(fmt)

        timestamp = os.path.getmtime(file_path)
        lastDateFileModified = datetime.fromtimestamp(timestamp).strftime(fmt)

        print(f"Now = {dateNow}")
        print(f"file timestamp {timestamp}")
        print(f"{file_path} last modified {lastDateFileModified}")

        if dateNow == lastDateFileModified:
            print(F"{file_path} atualizado Hoje!")
            return True
        else:
            print(F"{file_path} não atualizado Hoje!")
            return False
    else:
        print(F"{file_path} não encontrado!")
        return False


def get_file_lines(file_path: str) -> list[str]:
    file = open(file_path, mode='r')
    lines = file.readlines()
    file.close()
    return lines