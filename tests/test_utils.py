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


@pytest.mark.parametrize(
    "args, expected",
    [
        ({"path": "/path/to/folder"}, "folder"),
        ({"path": "/path/to/folder/"}, ""),
        ({"path": "user/other_path/some-folder/test"}, "test"),
        ({"path": "user_dir"}, "user_dir"),
        ({"path": "/path with spaces/in name/my destiny"}, "my destiny"),
        ({}, "rasa-model-report"),
        ({"path": None}, "rasa-model-report"),
        ({"path": ""}, "rasa-model-report"),
    ]
)
def test_get_project_name(args, expected):
    assert utils.get_project_name(**args) == expected


@pytest.mark.parametrize(
    "args, expected",
    [
        ({"value": 0.123312, "scale": 10}, "1.2"),
        ({"value": 98.6, "scale": 1}, "98.6"),
        ({"value": 0.4629, "scale": 100}, "46.3"),
        ({"value": 0.001}, "0"),
        ({"value": 0.3}, "0.3"),
        ({"value": 0.09}, "0.1"),
        ({"value": 90.5, "scale": 0.1}, "9.1"),
        ({"value": 0.001, "scale": 100}, "0.1"),

        # Other precisions
        ({"value": 10, "scale": 1, "precision": 2}, "10"),
        ({"value": 0.9999973454492488, "scale": 10, "precision": 2}, "10"),
        ({"value": 39.591231, "scale": 1, "precision": 2}, "39.59"),
        ({"value": 0.05281239, "scale": 1, "precision": 1}, "0.1"),
        ({"value": 0.5219483, "scale": 10, "precision": 2}, "5.22"),
        ({"value": 0.4, "scale": 100, "precision": 3}, "40"),
        ({"value": 0.511232, "scale": 100, "precision": 3}, "51.123"),
        ({"value": 0.85, "scale": 100, "precision": 2}, "85"),
        ({"value": 0.12239432, "scale": 100, "precision": 5}, "12.23943"),
        ({"value": 19.51, "scale": 1, "precision": 4}, "19.5100"),
        ({"value": 19.51, "scale": 1, "precision": 0}, "20"),
        ({"value": 0.56831, "scale": 100, "precision": 0}, "57"),
        ({"value": 0.731, "scale": 10, "precision": 0}, "7"),

        # Invalid scales
        ({"value": 10, "scale": 0}, 10),
        ({"value": 0.001, "scale": "test"}, 0.001),

        # Invalid values
        ({"value": "-", "scale": 100}, "-"),
        ({"value": "test", "scale": 100}, "test"),
        ({"value": None, "scale": 100}, None),
        ({"value": "100", "scale": 1}, "100"),

        # Invalid precisions
        ({"value": 0.85, "scale": 100, "precision": None}, "85"),
        ({"value": 123, "scale": 1, "precision": "2"}, "123"),
        ({"value": 59, "scale": 1, "precision": 0.5}, "59"),
        ({"value": 1.8473, "scale": 1, "precision": 10}, "1.85"),
        ({"value": 9.123123, "scale": 1, "precision": 6}, "9.12")
    ]
)
def test_change_scale(args, expected):
    assert utils.change_scale(**args) == expected


@pytest.mark.parametrize(
    "args, expected",
    [
        ({"value": 10, "scale": 10}, "🟢"),
        ({"value": 0.9}, "🟢"),
        ({"value": 98.6}, "🟢"),
        ({"value": 0.9012}, "🟢"),
        ({"value": 0.899}, "🟡"),
        ({"value": 0.75}, "🟡"),
        ({"value": 8, "scale": 10}, "🟡"),
        ({"value": 0.7}, "🟡"),
        ({"value": 0.69}, "🟠"),
        ({"value": 0.5}, "🟠"),
        ({"value": 5, "scale": 10}, "🟠"),
        ({"value": 0.39}, "🔴"),
        ({"value": 10, "scale": 100}, "🔴"),
        ({"value": 0.1}, "🔴"),
        ({"value": 0.01}, "🔴"),
        ({"value": 0.001}, "🔴"),
        ({"value": 0.1, "scale": 100}, "🔴"),
        ({"value": 0.0009}, "❌"),
        ({"value": 0}, "❌"),
        ({"value": 0, "scale": 100}, "❌"),

        # Invalid scales
        ({"value": -1}, "❌"),
        ({"value": None}, "❌"),
        ({"value": "10", "scale": 10}, "❌"),
        ({"value": "1"}, "❌"),
        ({"value": "-"}, "❌"),
        ({"value": "test", "scale": 100}, "❌"),
    ]
)
def test_get_color(args, expected):
    assert utils.get_color(**args) == expected


@pytest.mark.parametrize(
    "flag, expected",
    [
        (True, "✅"),
        (1, "✅"),
        ("teste", "✅"),
        (-1, "✅"),
        (False, "❌"),
        (0, "❌"),
    ]
)
def test_check(flag, expected):
    assert utils.check(flag) == expected


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
