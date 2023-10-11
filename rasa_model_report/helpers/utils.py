import datetime
import glob
import logging
import os
import re
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

import requests.exceptions
from requests.adapters import HTTPAdapter
from requests.adapters import Retry
from yaml import safe_load

from rasa_model_report.helpers import constants


def format_date() -> str:
    """
    Format the current date to the format DD/MM/YY hh:mm:ss.

    :return str: Date string.
    """
    return datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S")


def convert_to_date(date: str) -> datetime.datetime:
    """
    Format string in the format DD/MM/YY hh:mm:ss to the datetime type.

    :param date: Date string.
    :return datetime.datetime: Datetime object.
    """
    return datetime.datetime.strptime(date, "%d/%m/%y %H:%M:%S")


def check(flag: bool) -> str:
    """
    Converts a boolean to an icon.

    :param flag: A boolean flag.
    :return str: A icon.
    """
    return "✅" if flag else "❌"


def get_color(value: float, scale: int = 1) -> str:
    """
    Returns a colored icon according to the value.

    :param value: Float value.
    :param scale: Scale that the value is on.
    :return str: A icon.
    """
    if isinstance(value, (float, int)):
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
    return "❌"


def change_scale(value: float, scale: int = 1, precision: int = 1) -> str:
    """
    Change the value scale and rounds it to display in string format.

    :param value: Value that will be changed to scale and rounds it.
    :param scale: Scale that will be applied.
    :param precision: Value precision.
    :return str: Value on the new scale and precision.
    """
    precision = precision if isinstance(precision, int) and 5 >= precision >= 0 else constants.GRADE_PRECISION
    if (
        isinstance(value, (float, int)) and
        isinstance(scale, (float, int)) and
        scale != 0
    ):
        new_value = value * scale
        if new_value >= 1 and new_value % int(new_value) == 0:
            return str(int(new_value))
        elif re.search(r"\.0$", f"{new_value:.{precision}f}"):
            return "0"
        else:
            return f"{new_value:.{precision}f}"
    return value


def get_project_name(path: Optional[str] = None) -> str:
    """
    Returns the project folder's name.

    :param path: Project path. If not informed, the current path will be used.
    :return str: Project folder's name.
    """
    directory_path = path or os.getcwd()
    return os.path.basename(directory_path)


def request(url: str, method: str = "GET", json: dict = {}) -> Optional[requests.Response]:
    """
    Function that makes requests.

    :param url: URL.
    :param method: Request method (default: "GET").
    :param json: JSON body request (default: {}).
    :return requests.Response: Response object.
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
    :return Union[dict, list]: Data in list or dict format.
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
    :return list: Difference between l1 and l2.
    """
    set_l2 = set(l2)
    return [element for element in l1 if element not in set_l2]


def path_to(origin_path: str, destiny_path: str) -> str:
    """
    Return path to *destiny_path* from *origin_path*.

    :param origin_path: Origin path
    :param destiny_path: Destiny path
    :return str: Path to *destiny_path* from *origin_path*
    """
    undo_path = ""
    destiny_path = remove_duplicate_slashs(destiny_path)
    origin_path = remove_duplicate_slashs(origin_path)
    origin_path = origin_path[:-1] if origin_path[-1] == "/" else origin_path
    temp_path = origin_path
    while not destiny_path.startswith(temp_path):
        temp_path = temp_path.split("/")[:-1]
        temp_path = "/".join(temp_path)
        undo_path += "../"
    else:
        temp_path = destiny_path.replace(temp_path, undo_path, 1)
        temp_path = remove_duplicate_slashs(temp_path)
        if temp_path:
            temp_path = temp_path + "/" if temp_path[-1] != "/" else temp_path
            temp_path = temp_path.replace("/", "", 1) if temp_path[0] == "/" else temp_path
        return temp_path


def remove_duplicate_slashs(text: str) -> str:
    """
    Remove duplicate slashs from string. Usually used in paths.

    :param text: Text string.
    :return str: Text without duplicate slashs.
    """
    return re.sub(r"\/+", "/", text)


def count_stories_and_rules(rasa_path: str) -> Dict[str, int]:
    """
    Count the number of stories and rules.

    :param rasa_path: Rasa project path.
    :return: Dictionary with the number of stories and rules.
    """
    data = {
        "rules": 0,
        "stories": 0
    }
    files = glob.glob(f"{rasa_path}/data/**/*yml", recursive=True)
    for file in files:
        file_data = load_yaml_file(file)
        data.update({
            "rules": data["rules"] + len(file_data.get("rules", [])),
            "stories": data["stories"] + len(file_data.get("stories", []))
        })
    return data


def get_current_version() -> str:
    """
    Get current version from setup.py file.

    :return: Current version.
    """
    file = open("setup.py")
    data = file.read()
    version = re.search(r"version=\"(\d+\.\d+\.\d+)\"", data)
    file.close()
    return version.group(1) if version else "0.0.0"
