import os.path

import pytest
import responses

import tests.utils as utils
from src.rasa_model_report.controllers.ModelReport import ModelReport
from src.rasa_model_report.controllers.NluController import NluController


@responses.activate
def load_controllers(rasa_path):
    output_path = "./tests"
    project_name = "test-project"
    version = "0.0.0"
    utils.load_mock_payloads()
    model_report = ModelReport(rasa_path, output_path, project_name, version)
    nlu_controller = NluController(rasa_path, output_path, project_name, version)
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
    assert model_report.project == "test-project"
    assert model_report.version == "0.0.0"
    assert model_report.dirs["RASA_PATH"] == rasa_path
    assert model_report.dirs["RESULTS_PATH"] == f"{rasa_path}/results"
    assert model_report.dirs["OUTPUT_DIR"] == "./tests"
    assert model_report.dirs["INTENT_HISTOGRAM"] == "intent_histogram.png"
    assert model_report.dirs["INTENT_MATRIX"] == "intent_confusion_matrix.png"
    assert model_report.dirs["ENTITY_HISTOGRAM"] == "DIETClassifier_histogram.png"
    assert model_report.dirs["ENTITY_MATRIX"] == "DIETClassifier_confusion_matrix.png"
    assert model_report.dirs["STORY_MATRIX"] == "story_confusion_matrix.png"


def test_model_report_with_nlu():
    model_report = pytest.model_report
    model_report.markdown.nlu = pytest.nlu_controller
    model_report.generate_report()
    assert os.path.isfile(model_report.markdown.OUTPUT_REPORT_FILE)
    assert os.path.isfile(model_report.markdown.json.OVERVIEW_REPORT)


def test_model_report_with_invalid_path(rasa_path):
    model_report = pytest.model_report
    utils.remove_generated_files(rasa_path)
    model_report.dirs["RESULTS_PATH"] = "invalid/path"
    model_report.generate_report()
    assert not os.path.isfile(model_report.markdown.OUTPUT_REPORT_FILE)
    assert not os.path.isfile(model_report.markdown.json.OVERVIEW_REPORT)
