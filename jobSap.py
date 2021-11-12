from pandas import DataFrame
from unidecode import unidecode
from fileUtils import file_exists, get_file_lines


def get_data_frame_from_text_job_file(job_file_path : str) -> DataFrame:
    data_frame = DataFrame()

    try:
        if file_exists(job_file_path):
            file_lines = get_file_lines(job_file_path)
            eligible_lines = list(filter(_filter_eligle_lines_func, file_lines))
            lines = list(map(_map_split_lines_by_char,eligible_lines))
            data_frame = _get_data_frame_from_lines(lines)
            
    except Exception as e:
        print(e)

    return data_frame


def _filter_eligle_lines_func(line : str) -> bool:
    if line[0] == '|' and line[1] != '-':
        return True
    return False


def _map_split_lines_by_char(line : str, char: str = '|') -> list:
    split = line.split(char)
    split = list(map(lambda value : unidecode(value.strip()), split))
    del split[0]
    del split[-1]
    return split


def _get_data_frame_from_lines(lines : list) -> DataFrame:
    columns = lines[0]
    del lines[0]

    for index, el in enumerate(lines):
        if el == columns:
            del lines[index]

    data_frame = DataFrame(lines, columns=columns)
    return data_frame