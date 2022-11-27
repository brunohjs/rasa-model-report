import os

import pytest

import tests.utils as utils
from src.rasa_model_report.controllers.CsvController import CsvController


@pytest.fixture(autouse=True)
def execute_before_each_test(rasa_path):
    output_path = "./tests"
    project_name = "test-project"
    version = "0.0.0"
    csv_controller = CsvController(rasa_path, output_path, project_name, version)
    pytest.csv_controller = csv_controller
    yield
    utils.remove_generated_files(rasa_path)


def test_init_csv_controller(rasa_path):
    csv_controller = pytest.csv_controller
    assert csv_controller.project == "test-project"
    assert csv_controller.version == "0.0.0"
    assert csv_controller.RASA_PATH == rasa_path
    assert csv_controller.OUTPUT_DIR == "./tests"
    assert csv_controller.NLU_PATH == f"{rasa_path}/data"
    assert csv_controller.RESULTS_PATH == f"{rasa_path}/results"
    assert csv_controller.CONFIG_REPORT == f"{rasa_path}/config.yml"


def test_save_csv():
    csv_controller = pytest.csv_controller
    csv_controller.save([["header_1", "header_2"], ["data_1", "data_1"]], pytest.file_name)
    assert os.path.isfile(f"{csv_controller.RESULTS_PATH}/{pytest.file_name}")


def test_save_csv_with_error():
    csv_controller = pytest.csv_controller
    os.rename(csv_controller.RESULTS_PATH, f"{csv_controller.RESULTS_PATH}2")
    csv_controller.save([["header_1", "header_2"], ["data_1", "data_1"]], pytest.file_name)
    assert not os.path.isfile(f"{csv_controller.RESULTS_PATH}/{pytest.file_name}")
    os.rename(f"{csv_controller.RESULTS_PATH}2", csv_controller.RESULTS_PATH)
