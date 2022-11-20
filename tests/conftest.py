import glob

import pytest

import tests.utils as utils
from src.rasa_model_report.controllers.Controller import Controller
from src.rasa_model_report.controllers.CsvController import CsvController
from src.rasa_model_report.controllers.JsonController import JsonController


def pytest_generate_tests(metafunc):
    rasa_dirs = glob.glob("tests/rasa_mock/*")
    metafunc.fixturenames.append('rasa_path')
    metafunc.parametrize('rasa_path', rasa_dirs)


@pytest.fixture(autouse=True)
def execute_before_each_test(rasa_path):
    controller = Controller(rasa_path, "./tests", "test-project", "0.0.0")
    json_controller = JsonController(rasa_path, "./tests", "test-project", "0.0.0")
    csv_controller = CsvController(rasa_path, "./tests", "test-project", "0.0.0")
    pytest.controller = controller
    pytest.json_controller = json_controller
    pytest.csv_controller = csv_controller
    pytest.file_name = "test.csv"
    yield
    utils.remove_generated_files(rasa_path)
