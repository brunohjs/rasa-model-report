import datetime
from unittest import mock

import pytest
import requests.exceptions
import responses
from freezegun import freeze_time

from rasa_model_report.helpers.utils import change_scale
from rasa_model_report.helpers.utils import check
from rasa_model_report.helpers.utils import convert_to_date
from rasa_model_report.helpers.utils import format_date
from rasa_model_report.helpers.utils import get_color
from rasa_model_report.helpers.utils import get_project_name
from rasa_model_report.helpers.utils import list_diff
from rasa_model_report.helpers.utils import load_yaml_file
from rasa_model_report.helpers.utils import path_to
from rasa_model_report.helpers.utils import remove_duplicate_slashs
from rasa_model_report.helpers.utils import request
from tests import utils


@pytest.fixture(autouse=True)
def execute_before_each_test():
    pass


def test_get_project_name():
    assert get_project_name("/path/to/folder") == "folder"
    assert get_project_name("/path/to/folder/") == ""
    assert get_project_name("user/other_path/some-folder/test") == "test"
    assert get_project_name("user_dir") == "user_dir"
    assert get_project_name("/path with spaces/in name/my destiny") == "my destiny"
    assert get_project_name() == "rasa-model-report"
    assert get_project_name("") == "rasa-model-report"


def test_change_scale():
    assert isinstance(change_scale(0.123312, 10), str)
    assert change_scale(0.123312, 10) == "1"
    assert change_scale(98.6, 1) == "98"
    assert change_scale(0.4629, 100) == "46"
    assert change_scale(90.5, 0.1) == "9"
    assert change_scale(0.001) == "0"
    assert change_scale(None) is None
    assert change_scale("-") == "-"
    assert change_scale("test", 100) == "test"


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
    assert get_color(0.001) == "🔴"
    assert get_color(0.1, 100) == "🔴"
    assert get_color(0.0009) == "❌"
    assert get_color(0) == "❌"
    assert get_color(0, 100) == "❌"
    assert get_color(-1) == "❌"
    assert get_color(None) == "❌"
    assert get_color("-") == "❌"
    assert get_color("test", 100) == "❌"


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


@responses.activate
def test_request_200():
    utils.load_mock_payloads()
    response = request("http://localhost:5005")
    assert response.status_code == 200


@responses.activate
def test_request_general_error():
    utils.load_mock_payloads()
    response = request("invalid url")
    assert response is None


@responses.activate
def test_request_connection_error():
    with mock.patch("requests.get", side_effect=requests.exceptions.ConnectionError()):
        response = request("http://localhost:5005")
        assert response is None


def test_load_yaml_file(rasa_path):
    # When file exist is expected a dict.
    assert isinstance(load_yaml_file(f"{rasa_path}/domain.yml"), dict)

    # When file doesn't exist and erro_flag is False is expected {} in return.
    assert load_yaml_file(f"{rasa_path}/file.not.exist", error_flag=False) == {}

    # When file doesn't exist and erro_flag is True is expected Exception.
    with pytest.raises(Exception):
        load_yaml_file(f"{rasa_path}/file.not.exist")


def test_list_diff():
    list_1 = [1, 2, 3, 4, 5]
    list_2 = [7, 6, 5, 4]
    assert list_diff(list_1, list_2) == [1, 2, 3]
    assert list_diff(list_2, list_1) == [7, 6]
    assert list_diff(list_2, list_diff(list_2, list_1)) == [5, 4]
    assert list_diff([], []) == []
    assert list_diff(list_1, []) == list_1
    assert list_diff([], list_1) == []
    assert list_diff(list_1, list_1) == []


def test_path_to():
    assert path_to("tests/mocks/rasa.v2/results/", "tests/mocks/rasa.v2/results") == ""
    assert path_to("tests/mocks/rasa.v2/results", "tests/mocks/rasa.v2/results") == ""
    assert path_to("tests/mocks/rasa.v2/results", "tests/mocks/rasa.v2/results/") == ""
    assert path_to("tests//mocks/rasa.v2/results", "tests/mocks/rasa.v2/results") == ""
    assert path_to("tests/mocks", "tests/mocks/rasa.v2/results") == "rasa.v2/results/"
    assert path_to("tests/mocks/rasa.v3", "tests/mocks/rasa.v2/results") == "../rasa.v2/results/"
    assert path_to("actions/", "tests/mocks/rasa.v2/results") == "../tests/mocks/rasa.v2/results/"
    assert path_to("actions", "tests/mocks/rasa.v2/results") == "../tests/mocks/rasa.v2/results/"
    assert path_to("actions/src/results", "tests/mocks/rasa.v2/results") == "../../../tests/mocks/rasa.v2/results/"
    assert path_to("actions/src/results/", "tests/mocks/rasa.v2/results") == "../../../tests/mocks/rasa.v2/results/"


def test_remove_duplicate_slash():
    assert remove_duplicate_slashs("tests//mocks/rasa.v2/results") == "tests/mocks/rasa.v2/results"
    assert remove_duplicate_slashs("tests///mocks/rasa.v2//results//") == "tests/mocks/rasa.v2/results/"
    assert remove_duplicate_slashs("tests////mocks/rasa.v2/results/") == "tests/mocks/rasa.v2/results/"
    assert remove_duplicate_slashs("tests////mocks/////rasa.v2/results/") == "tests/mocks/rasa.v2/results/"
    assert remove_duplicate_slashs("///") == "/"
