import datetime
from unittest import mock

import pytest
import requests.exceptions
import responses
from freezegun import freeze_time

from rasa_model_report.helpers import utils
from tests import utils as test_utils


@pytest.fixture(autouse=True)
def execute_before_each_test():
    pass


def test_get_project_name():
    assert utils.get_project_name("/path/to/folder") == "folder"
    assert utils.get_project_name("/path/to/folder/") == ""
    assert utils.get_project_name("user/other_path/some-folder/test") == "test"
    assert utils.get_project_name("user_dir") == "user_dir"
    assert (
        utils.get_project_name("/path with spaces/in name/my destiny") == "my destiny"
    )
    assert utils.get_project_name() == "rasa-model-report"
    assert utils.get_project_name("") == "rasa-model-report"


def test_change_scale():
    assert isinstance(utils.change_scale(0.123312, 10), str)
    assert utils.change_scale(0.123312, 10) == "1.2"
    assert utils.change_scale(98.6, 1) == "98.6"
    assert utils.change_scale(0.4629, 100) == "46.3"
    assert utils.change_scale(0.001) == "0"
    assert utils.change_scale(0.3) == "0.3"
    assert utils.change_scale(0.09) == "0.1"
    assert utils.change_scale(90.5, 0.1) == "9.1"
    assert utils.change_scale(0.001, 0.1) == "0"

    # Other precisions
    assert utils.change_scale(10, 1, 2) == "10"
    assert utils.change_scale(39.591231, 1, 2) == "39.59"
    assert utils.change_scale(0.05281239, 1, 1) == "0.1"
    assert utils.change_scale(0.5219483, 10, 2) == "5.22"
    assert utils.change_scale(0.4, 100, 3) == "40"
    assert utils.change_scale(0.511232, 100, 3) == "51.123"
    assert utils.change_scale(0.85, 100, 2) == "85"
    assert utils.change_scale(0.12239432, 100, 5) == "12.23943"
    assert utils.change_scale(19.51, 1, 4) == "19.5100"
    assert utils.change_scale(19.51, 1, 0) == "20"
    assert utils.change_scale(0.56831, 100, 0) == "57"
    assert utils.change_scale(0.731, 10, 0) == "7"

    # Invalid scales
    assert utils.change_scale(10, 0) == 10
    assert utils.change_scale(0.001, "test") == 0.001

    # Invalid values
    assert utils.change_scale("-") == "-"
    assert utils.change_scale("test", 100) == "test"
    assert utils.change_scale(None) is None
    assert utils.change_scale("100", 1) == "100"

    # Invalid precisions
    assert utils.change_scale(0.85, 100, None) == "85"
    assert utils.change_scale(123, 1, "2") == "123"
    assert utils.change_scale(59, 1, 0.5) == "59"
    assert utils.change_scale(1.8473, 1, 10) == "1.85"
    assert utils.change_scale(9.123123, 1, 6) == "9.12"


def test_get_color():
    assert utils.get_color(10, 10) == "🟢"
    assert utils.get_color(0.98) == "🟢"
    assert utils.get_color(0.9012) == "🟢"
    assert utils.get_color(0.899) == "🟡"
    assert utils.get_color(0.75) == "🟡"
    assert utils.get_color(8, 10) == "🟡"
    assert utils.get_color(0.7) == "🟡"
    assert utils.get_color(0.69) == "🟠"
    assert utils.get_color(0.5) == "🟠"
    assert utils.get_color(5, 10) == "🟠"
    assert utils.get_color(0.39) == "🔴"
    assert utils.get_color(10, 100) == "🔴"
    assert utils.get_color(0.1) == "🔴"
    assert utils.get_color(0.01) == "🔴"
    assert utils.get_color(0.001) == "🔴"
    assert utils.get_color(0.1, 100) == "🔴"
    assert utils.get_color(0.0009) == "❌"
    assert utils.get_color(0) == "❌"
    assert utils.get_color(0, 100) == "❌"

    # Invalid values
    assert utils.get_color(-1) == "❌"
    assert utils.get_color(None) == "❌"
    assert utils.get_color("10", 10) == "❌"
    assert utils.get_color("1") == "❌"
    assert utils.get_color("-") == "❌"
    assert utils.get_color("test", 100) == "❌"


def test_check():
    assert utils.check(True) == "✅"
    assert utils.check(1) == "✅"
    assert utils.check("teste") == "✅"
    assert utils.check(-1) == "✅"
    assert utils.check(False) == "❌"
    assert utils.check(0) == "❌"


def test_convert_to_date_checking_return_type():
    assert isinstance(utils.convert_to_date("01/01/01 00:00:00"), datetime.datetime)


def test_convert_to_date_with_invalid_format():
    with pytest.raises(ValueError):
        utils.convert_to_date("01/01/2001 00:00:00")
        utils.convert_to_date("")


def test_convert_to_date():
    date = utils.convert_to_date("01/02/03 04:05:06")
    assert date.day == 1
    assert date.month == 2
    assert date.year == 2003
    assert date.hour == 4
    assert date.minute == 5
    assert date.second == 6


@freeze_time("02-01-2003")
def test_format_date():
    assert utils.format_date() == "01/02/03 00:00:00"


@responses.activate
def test_request_200():
    test_utils.load_mock_payloads()
    response = utils.request("http://localhost:5005")
    assert response.status_code == 200


@responses.activate
def test_request_general_error():
    test_utils.load_mock_payloads()
    response = utils.request("invalid url")
    assert response is None


@responses.activate
def test_request_connection_error():
    with mock.patch("requests.get", side_effect=requests.exceptions.ConnectionError()):
        response = utils.request("http://localhost:5005")
        assert response is None


def test_load_yaml_file(rasa_path):
    # When file exist is expected a dict.
    assert isinstance(utils.load_yaml_file(f"{rasa_path}/domain.yml"), dict)

    # When file doesn't exist and erro_flag is False is expected {} in return.
    assert utils.load_yaml_file(f"{rasa_path}/file.not.exist", error_flag=False) == {}

    # When file doesn't exist and erro_flag is True is expected Exception.
    with pytest.raises(Exception):
        utils.load_yaml_file(f"{rasa_path}/file.not.exist")


def test_list_diff():
    list_1 = [1, 2, 3, 4, 5]
    list_2 = [7, 6, 5, 4]
    assert utils.list_diff(list_1, list_2) == [1, 2, 3]
    assert utils.list_diff(list_2, list_1) == [7, 6]
    assert utils.list_diff(list_2, utils.list_diff(list_2, list_1)) == [5, 4]
    assert utils.list_diff([], []) == []
    assert utils.list_diff(list_1, []) == list_1
    assert utils.list_diff([], list_1) == []
    assert utils.list_diff(list_1, list_1) == []


@pytest.mark.parametrize(
    "origin_path, destiny_path, expected",
    [
        ("tests/mocks/rasa.v2/results/", "tests/mocks/rasa.v2/results/", ""),
        ("tests/mocks/rasa.v2/results", "tests/mocks/rasa.v2/results", ""),
        ("tests/mocks/rasa.v2/results", "tests/mocks/rasa.v2/results/", ""),
        ("tests//mocks/rasa.v2/results", "tests/mocks/rasa.v2/results", ""),
        ("tests/mocks", "tests/mocks/rasa.v2/results", "rasa.v2/results/"),
        ("tests/mocks/rasa.v3", "tests/mocks/rasa.v2/results", "../rasa.v2/results/"),
        ("actions/", "tests/mocks/rasa.v2/results", "../tests/mocks/rasa.v2/results/"),
        ("actions", "tests/mocks/rasa.v2/results", "../tests/mocks/rasa.v2/results/"),
        (
            "actions/src/results",
            "tests/mocks/rasa.v2/results",
            "../../../tests/mocks/rasa.v2/results/",
        ),
        (
            "actions/src/results/",
            "tests/mocks/rasa.v2/results",
            "../../../tests/mocks/rasa.v2/results/",
        ),
    ],
)
def test_path_to(origin_path, destiny_path, expected):
    assert utils.path_to(origin_path, destiny_path) == expected


@pytest.mark.parametrize(
    "path, expected",
    [
        ("tests//mocks/rasa.v2/results", "tests/mocks/rasa.v2/results"),
        ("tests///mocks/rasa.v2//results//", "tests/mocks/rasa.v2/results/"),
        ("tests////mocks/rasa.v2/results/", "tests/mocks/rasa.v2/results/"),
        ("tests////mocks/////rasa.v2/results/", "tests/mocks/rasa.v2/results/"),
        ("///", "/"),
        ("./", "./")
    ],
)
def test_remove_duplicate_slash(path, expected):
    assert utils.remove_duplicate_slashs(path) == expected


def test_count_stories_and_rules(rasa_path):
    data = utils.count_stories_and_rules(rasa_path)
    assert data.keys() == {"stories", "rules"}
    assert isinstance(data["stories"], int)
    assert isinstance(data["rules"], int)


def test_get_current_version():
    version = utils.get_current_version()
    assert isinstance(version, str)
    assert len(version.split(".")) == 3
