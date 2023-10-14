import sys
import unittest.mock

import pytest

from scripts import release


@pytest.fixture(autouse=True)
def execute_before_each_test(rasa_path):
    pass


@pytest.mark.parametrize(
    "current_version, args, expected",
    [
        ("0.0.1", [], "0.0.2"),
        ("0.0.1", ["patch"], "0.0.2"),
        ("0.0.1", ["minor"], "0.1.0"),
        ("1.4.0", ["minor"], "1.5.0"),
        ("0.0.1", ["major"], "1.0.0"),
        ("1.0.1", ["major"], "2.0.0"),
        ("10.5.1", ["major"], "11.0.0"),
        ("5.4.1", ["major", "beta"], "6.0.0b1"),
        ("9.0.0", ["major", "beta"], "10.0.0b1"),
        ("0.0.0", ["minor", "beta"], "0.1.0b1"),
        ("2.2.0", ["patch", "beta"], "2.2.1b1"),
        ("1.0.6b5", ["patch", "beta"], "1.0.6b6"),
        ("1.0.6b11", ["minor", "beta"], "1.0.6b12"),
        ("1.0.6b9", ["major", "beta"], "1.0.6b10"),
        ("1.0.6b9", ["test", "beta"], "1.0.6b10"),
        ("1.0.6b9", ["beta"], "1.0.6b10"),
    ],
)
def test_get_new_version(current_version, args, expected):
    unittest.mock.patch("scripts.release.get_latest_version", return_value=current_version).start()
    sys.argv = ["release.py"] + args
    try:
        assert release.get_new_version() == expected
    except Exception:
        with pytest.raises(Exception):
            release.get_new_version()
