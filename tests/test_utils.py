import datetime

import pytest
from freezegun import freeze_time

from src.rasa_model_report.helpers.utils import check
from src.rasa_model_report.helpers.utils import convert_to_date
from src.rasa_model_report.helpers.utils import format_date
from src.rasa_model_report.helpers.utils import get_color
from src.rasa_model_report.helpers.utils import get_project_name
from src.rasa_model_report.helpers.utils import scale


@pytest.fixture(autouse=True)
def execute_before_each_test(rasa_path):
    pass


def test_get_project_name():
    assert get_project_name("/path/to/folder") == "folder"
    assert get_project_name("/path/to/folder/") == ""
    assert get_project_name("user/other_path/some-folder/test") == "test"
    assert get_project_name("user_dir") == "user_dir"
    assert get_project_name("/path with spaces/in name/my destiny") == "my destiny"
    assert get_project_name() == "rasa-model-report"
    assert get_project_name("") == "rasa-model-report"


def test_scale():
    assert isinstance(scale(0.123312, 10), str)
    assert scale(0.123312, 10) == "1"
    assert scale(98.6, 1) == "98"
    assert scale(0.4629, 100) == "46"
    assert scale(90.5, 0.1) == "9"
    assert scale(0.001) == "0"


def test_get_color():
    assert get_color(0.98) == "🟢"
    assert get_color(0.9012) == "🟢"
    assert get_color(0.899) == "🟡"
    assert get_color(0.75) == "🟡"
    assert get_color(8, 10) == "🟡"
    assert get_color(0.7) == "🟡"
    assert get_color(0.69) == "🟠"
    assert get_color(0.5) == "🟠"
    assert get_color(5, 10) == "🟠"
    assert get_color(0.39) == "🔴"
    assert get_color(10, 100) == "🔴"
    assert get_color(0.1) == "🔴"
    assert get_color(0.01) == "🔴"
    assert get_color(0.001) == "❌"
    assert get_color(0.1, 100) == "❌"
    assert get_color(0) == "❌"
    assert get_color(0, 100) == "❌"
    assert get_color(-1) == "❌"


def test_check():
    assert check(True) == "✅"
    assert check(1) == "✅"
    assert check("teste") == "✅"
    assert check(-1) == "✅"
    assert check(False) == "❌"
    assert check(0) == "❌"


def test_convert_to_date_checking_return_type():
    assert isinstance(convert_to_date("01/01/01 00:00:00"), datetime.datetime)


def test_convert_to_date_with_invalid_format():
    with pytest.raises(ValueError):
        convert_to_date("01/01/2001 00:00:00")
        convert_to_date("")


def test_convert_to_date():
    date = convert_to_date("01/02/03 04:05:06")
    assert date.day == 1
    assert date.month == 2
    assert date.year == 2003
    assert date.hour == 4
    assert date.minute == 5
    assert date.second == 6


@freeze_time("02-01-2003")
def test_format_date():
    assert format_date() == "01/02/03 00:00:00"
