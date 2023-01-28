import datetime
import logging
import os
from typing import List
from typing import Optional
from typing import Union

import requests.exceptions
from requests.adapters import HTTPAdapter
from requests.adapters import Retry
from yaml import safe_load


def format_date() -> str:
    """
    Format the current date to the format DD/MM/YY hh:mm:ss.

    :return: Date string.
    """
    now = datetime.datetime.now()
    return now.strftime("%d/%m/%y %H:%M:%S")


def convert_to_date(date: str) -> datetime.datetime:
    """
    Format string in the format DD/MM/YY hh:mm:ss to the datetime type.

    :param date: Date string.
    :return: Datetime object.
    """
    return datetime.datetime.strptime(date, "%d/%m/%y %H:%M:%S")


def check(flag: bool) -> str:
    """
    Converts a boolean to an icon.

    :param flag: A boolean flag.
    :return: A icon.
    """
    return "✅" if flag else "❌"


def get_color(value: float, scale: int = 1) -> str:
    """
    Returns a colored icon according to the value.

    :param value: Float value.
    :param scale: Scale that the value is on.
    :return: A icon.
    """
    if scale > 1:
        value /= scale
    if value >= 0.9:
        return "🟢"
    elif value >= 0.7:
        return "🟡"
    elif value >= 0.4:
        return "🟠"
    elif value >= 0.001:
        return "🔴"
    else:
        return "❌"


def change_scale(value: float, scale: int = 1) -> str:
    """
    Change the value scale and rounds it to display in string format.

    :param value: Value that will be changed to scale and rounds it.
    :param scale: Scale that will be applied.
    :return: Value on the new scale.
    """
    return f"{int(value * scale)}"


def get_project_name(path: Optional[str] = None) -> str:
    """
    Returns the project folder's name.

    :param path: Project path. If not informed, the current path will be used.
    :return: Project folder's name.
    """
    if path:
        return os.path.basename(path)
    directory_path = os.getcwd()
    return os.path.basename(directory_path)


def request(url: str, method: str = "GET", json: dict = {}) -> Optional[requests.Response]:
    """
    Function that makes requests.

    :param url: URL.
    :param method: Request method (default: "GET").
    :param json: JSON body request (default: {}).
    :return: Response object.
    """
    response = None
    try:
        session = requests.Session()
        retries = Retry(total=2, backoff_factor=3)
        session.mount("http://", HTTPAdapter(max_retries=retries))
        response = session.request(method=method, url=url, json=json)
    except (
        requests.exceptions.ConnectionError,
        requests.exceptions.Timeout,
        requests.exceptions.RequestException
    ) as error:
        logging.warning(f"Error connecting to {url}. Message: {error}")
    finally:
        return response


def load_yaml_file(filename: str, error_flag: bool = True) -> Union[dict, list]:
    """
    Load data from YAML file.

    :param filename: YAML filename.
    :param error_flag: If True, an exception will be raised when the file isn't found (default: True).
    :return: Data in list or dict format.
    """
    if os.path.isfile(filename):
        file = open(filename, encoding="utf-8")
        data = safe_load(file)
        file.close()
        logging.info(f"{filename} file loaded successfully.")
        return data
    else:
        message = f"{filename} file not found."
        if error_flag:
            logging.error(message)
            raise Exception(message)
        else:
            logging.warning(message)
            return {}


def list_diff(l1: List[str], l2: List[str]) -> List[str]:
    """
    Returns a list with the difference between l1 and l2 (l1 - l2).

    :param l1: First list.
    :param l2: Second list.
    :return: Difference between l1 and l2.
    """
    return [element for element in l1 if element not in l2]
