import pytest
import responses

from rasa_model_report.controllers.model_report import ModelReport
from rasa_model_report.controllers.nlu_controller import NluController
from tests import utils


@responses.activate
def load_controllers(rasa_path):
    output_path = "./tests"
    project_name = "test-project"
    project_version = "0.0.0"
    rasa_version = "0.0.0"
    utils.load_mock_payloads()
    model_report = ModelReport(rasa_path, output_path, project_name, rasa_version, project_version)
    nlu_controller = NluController(rasa_path, output_path, project_name, project_version)
    pytest.model_report = model_report
    pytest.nlu_controller = nlu_controller


@pytest.fixture(autouse=True)
def execute_before_each_test(rasa_path):
    load_controllers(rasa_path)
    pytest.file_name = "test.csv"
    yield
    utils.remove_generated_files(rasa_path)


def test_init_model_report(rasa_path):
    model_report = pytest.model_report
    assert model_report.project_name == "test-project"
    assert model_report.project_version == "0.0.0"
    assert model_report.rasa_version == "0.0.0"
    assert model_report.output_format == "md"
