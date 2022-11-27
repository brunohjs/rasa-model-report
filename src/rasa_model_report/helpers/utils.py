import datetime
import os
from typing import Optional
from typing import Union


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


def get_color(value: Union[float, int], scale: int = 1) -> str:
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
    elif value >= 0.01:
        return "🔴"
    else:
        return "❌"


def scale(value: float, scale: int = 1) -> str:
    """
    Change the value scale and rounds it to display in string format.

    :param value: Value that will be changed to scale and rounds it.
    :param int scale: Scale that will be applied.
    :return str: Value on the new scale.
    """
    return f"{int(value * scale)}"


def get_project_name(path: Optional[str] = None) -> str:
    """
    Function that returns the project folder's name.

    :param str: Project path. If not informed, the current path will be used.
    :return str: Project folder's name.
    """
    if path:
        return os.path.basename(path)
    directory_path = os.getcwd()
    return os.path.basename(directory_path)
