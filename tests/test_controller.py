import pytest


def test_init_controller(rasa_path):
    controller = pytest.controller
    assert controller.project == "test-project"
    assert controller.version == "0.0.0"
    assert controller.RASA_PATH == rasa_path
    assert controller.OUTPUT_DIR == "./tests"
    assert controller.NLU_PATH == f"{rasa_path}/data"
    assert controller.RESULTS_PATH == f"{rasa_path}/results"
    assert controller.CONFIG_REPORT == f"{rasa_path}/config.yml"
