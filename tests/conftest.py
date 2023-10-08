import glob

import pytest
import responses

from rasa_model_report.controllers.controller import Controller
from rasa_model_report.controllers.csv_controller import CsvController
from rasa_model_report.controllers.e2e_coverage_controller import E2ECoverageController
from rasa_model_report.controllers.json_controller import JsonController
from rasa_model_report.controllers.markdown_controller import MarkdownController
from rasa_model_report.controllers.nlu_controller import NluController
from tests import utils


def pytest_generate_tests(metafunc):
    rasa_dirs = glob.glob("tests/mocks/rasa.v*")
    metafunc.fixturenames.append("rasa_path")
    metafunc.parametrize("rasa_path", rasa_dirs)


@pytest.fixture(autouse=True)
def execute_before_each_test(rasa_path):
    load_controllers(rasa_path)
    pytest.file_name = "test.csv"
    yield
    utils.remove_generated_files(rasa_path)


@responses.activate
def load_controllers(rasa_path):
    output_path = "./tests"
    actions_path = None
    project_name = "test-project"
    project_version = "0.0.0"
    rasa_version = "0.0.0"
    exclude = []
    utils.load_mock_payloads()
    controller = Controller(rasa_path, output_path, project_name, project_version)
    json_controller = JsonController(
        rasa_path, output_path, project_name, project_version
    )
    csv_controller = CsvController(
        rasa_path, output_path, project_name, project_version
    )
    nlu_controller = NluController(
        rasa_path, output_path, project_name, project_version
    )
    e2e_coverage_controller = E2ECoverageController(
        rasa_path, output_path, actions_path, exclude, project_name, project_version
    )
    markdown_controller = MarkdownController(
        rasa_path, output_path, project_name, rasa_version, project_version
    )
    pytest.controller = controller
    pytest.json_controller = json_controller
    pytest.csv_controller = csv_controller
    pytest.nlu_controller = nlu_controller
    pytest.e2e_coverage_controller = e2e_coverage_controller
    pytest.markdown_controller = markdown_controller
