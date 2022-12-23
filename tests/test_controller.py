import pytest


def test_init_controller(rasa_path):
    controller = pytest.controller
    assert controller.project_name == "test-project"
    assert controller.project_version == "0.0.0"
    assert controller.rasa_path == rasa_path
    assert controller.output_path == "./tests"
    assert controller.nlu_path == f"{rasa_path}/data"
    assert controller.results_path == f"{rasa_path}/results"
    assert controller.config_report_path == f"{rasa_path}/config.yml"
