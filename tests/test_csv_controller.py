import os

import pytest

from rasa_model_report.controllers.csv_controller import CsvController
from tests import utils


@pytest.fixture(autouse=True)
def execute_before_each_test(rasa_path):
    output_path = "./tests"
    project_name = "test-project"
    project_version = "0.0.0"
    csv_controller = CsvController(rasa_path, output_path, project_name, project_version)
    pytest.csv_controller = csv_controller
    yield
    utils.remove_generated_files(rasa_path)


def test_init_csv_controller(rasa_path):
    csv_controller = pytest.csv_controller
    assert csv_controller.project_name == "test-project"
    assert csv_controller.project_version == "0.0.0"
    assert csv_controller.rasa_path == rasa_path
    assert csv_controller.output_path == "./tests"
    assert csv_controller.nlu_path == f"{rasa_path}/data"
    assert csv_controller.results_path == f"{rasa_path}/results"
    assert csv_controller.config_report_path == f"{rasa_path}/config.yml"


def test_save_csv():
    csv_controller = pytest.csv_controller
    csv_controller.save([["header_1", "header_2"], ["data_1", "data_1"]], pytest.file_name)
    assert os.path.isfile(f"{csv_controller.results_path}/{pytest.file_name}")


def test_save_csv_with_error():
    csv_controller = pytest.csv_controller
    os.rename(csv_controller.results_path, f"{csv_controller.results_path}2")
    csv_controller.save([["header_1", "header_2"], ["data_1", "data_1"]], pytest.file_name)
    assert not os.path.isfile(f"{csv_controller.results_path}/{pytest.file_name}")
    os.rename(f"{csv_controller.results_path}2", csv_controller.results_path)
