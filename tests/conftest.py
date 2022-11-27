import glob

import pytest
import responses

import tests.utils as utils
from src.rasa_model_report.controllers.Controller import Controller
from src.rasa_model_report.controllers.CsvController import CsvController
from src.rasa_model_report.controllers.JsonController import JsonController
from src.rasa_model_report.controllers.MarkdownController import MarkdownController
from src.rasa_model_report.controllers.NluController import NluController


def pytest_generate_tests(metafunc):
    rasa_dirs = glob.glob("tests/mocks/rasa.v*")
    metafunc.fixturenames.append('rasa_path')
    metafunc.parametrize('rasa_path', rasa_dirs)


@pytest.fixture(autouse=True)
def execute_before_each_test(rasa_path):
    load_controllers(rasa_path)
    pytest.file_name = "test.csv"
    yield
    utils.remove_generated_files(rasa_path)


@responses.activate
def load_controllers(rasa_path):
    output_path = "./tests"
    project_name = "test-project"
    version = "0.0.0"
    utils.load_mock_payloads()
    controller = Controller(rasa_path, output_path, project_name, version)
    json_controller = JsonController(rasa_path, output_path, project_name, version)
    csv_controller = CsvController(rasa_path, output_path, project_name, version)
    nlu_controller = NluController(rasa_path, output_path, project_name, version)
    markdown_controller = MarkdownController(rasa_path, output_path, project_name, version)
    pytest.controller = controller
    pytest.json_controller = json_controller
    pytest.csv_controller = csv_controller
    pytest.nlu_controller = nlu_controller
    pytest.markdown_controller = markdown_controller