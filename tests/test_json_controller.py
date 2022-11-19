import pytest


def test_init_json_controller(rasa_path):
    json_controller = pytest.json_controller
    assert json_controller.project == "test-project"
    assert json_controller.version == "0.0.0"
    assert json_controller.RASA_PATH == rasa_path
    assert json_controller.OUTPUT_DIR == "./tests"
    assert json_controller.NLU_PATH == f"{rasa_path}/data/**/**.yml"
    assert json_controller.RESULTS_PATH == f"{rasa_path}/results"
    assert json_controller.CONFIG_REPORT == f"{rasa_path}/config.yml"
    assert json_controller.INTENT_REPORT == f"{json_controller.RESULTS_PATH}/intent_report.json"
    assert json_controller.INTENT_ERRORS == f"{json_controller.RESULTS_PATH}/intent_errors.json"
    assert json_controller.ENTITY_REPORT == f"{json_controller.RESULTS_PATH}/DIETClassifier_report.json"
    assert json_controller.ENTITY_ERRORS == f"{json_controller.RESULTS_PATH}/DIETClassifier_errors.json"
    assert json_controller.STORY_REPORT == f"{json_controller.RESULTS_PATH}/story_report.json"
    assert json_controller.OVERVIEW_REPORT == f"{json_controller.RESULTS_PATH}/overview.json"
    assert json_controller.RASA_ENV_PATH == "../.env"
