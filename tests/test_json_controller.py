import os.path
import random

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


def test_load_json_file():
    json_controller = pytest.json_controller
    data = json_controller._load_json_file(json_controller.INTENT_REPORT)
    assert isinstance(data, dict)


def test_load_json_file_but_a_non_existent_file():
    json_controller = pytest.json_controller
    with pytest.raises(Exception):
        json_controller._load_json_file("path/that/does/not/exist.json")
        json_controller._load_json_file("path/that/does/not/exist.json", "warning")


def test_load_intents():
    json_controller = pytest.json_controller
    json_controller._load_intents()
    assert isinstance(json_controller.get_intents(), list)
    assert len(json_controller.get_intents()) > 0


def test_load_intents_but_a_non_existent_file():
    json_controller = pytest.json_controller
    json_controller.INTENT_REPORT = "path/that/does/not/exist.json"
    json_controller._load_intents()
    assert json_controller.get_intents() == []


def test_load_entities():
    json_controller = pytest.json_controller
    json_controller._load_entities()
    assert isinstance(json_controller.get_entities(), list)
    assert len(json_controller.get_entities()) > 0


def test_load_entities_but_a_non_existent_file():
    json_controller = pytest.json_controller
    json_controller.ENTITY_REPORT = "path/that/does/not/exist.json"
    json_controller._load_entities()
    assert json_controller.get_entities() == []


def test_load_overview():
    json_controller = pytest.json_controller
    json_controller._load_overview()
    assert isinstance(json_controller.get_overview(), dict)


def test_load_overview_if_exists():
    json_controller = pytest.json_controller
    json_controller._load_overview()
    json_controller.save_overview()
    json_controller._load_overview()
    assert isinstance(json_controller.get_overview(), dict)


def test_save_overview():
    json_controller = pytest.json_controller
    json_controller.save_overview()
    assert os.path.isfile(json_controller.OVERVIEW_REPORT)


def test_calculate_overall():
    json_controller = pytest.json_controller
    json_controller._calculate_overall()
    assert isinstance(json_controller.get_overview().get("overall"), (int, float))


def test_update_overview():
    json_controller = pytest.json_controller
    random_number = random.randint(0, 100)
    json_controller.update_overview({
        "nlu": random_number
    })
    assert json_controller.get_overview().get("nlu") == random_number


def test_dont_update_overview_when_not_a_dict_as_a_param():
    json_controller = pytest.json_controller
    overview = json_controller.get_overview()
    json_controller.update_overview(["test", "5"])
    assert json_controller.get_overview() == overview


def test_get_intents():
    json_controller = pytest.json_controller
    intents = json_controller.get_intents()
    intents.append({"test": "ok"})
    assert json_controller.get_intents() != intents
    assert isinstance(json_controller.get_intents(), list)


def test_get_intent_overview():
    json_controller = pytest.json_controller
    intent_overview = json_controller.get_intent_overview()
    intent_overview.update({"test": "ok"})
    assert json_controller.get_intent_overview() != intent_overview
    assert isinstance(json_controller.get_intent_overview(), dict)


def test_get_intent_errors():
    json_controller = pytest.json_controller
    intents = json_controller.get_intent_errors()
    intents.append({"test": "ok"})
    assert json_controller.get_intent_errors() != intents
    assert isinstance(json_controller.get_intent_errors(), list)


def test_get_entities():
    json_controller = pytest.json_controller
    entities = json_controller.get_entities()
    print(entities)
    entities.append({"test": "ok"})
    assert json_controller.get_entities() != entities
    assert isinstance(json_controller.get_entities(), list)


def test_get_entity_overview():
    json_controller = pytest.json_controller
    entity_overview = json_controller.get_entity_overview()
    entity_overview.update({"test": "ok"})
    assert json_controller.get_entity_overview() != entity_overview
    assert isinstance(json_controller.get_entity_overview(), dict)


def test_get_entity_errors():
    json_controller = pytest.json_controller
    entities = json_controller.get_entity_errors()
    entities.update({"test": "ok"})
    assert json_controller.get_entity_errors() != entities
    assert isinstance(json_controller.get_entity_errors(), dict)


def test_get_responses():
    json_controller = pytest.json_controller
    responses = json_controller.get_responses()
    responses.append({"test": "ok"})
    assert json_controller.get_responses() != responses
    assert isinstance(json_controller.get_responses(), list)


def test_get_response_overview():
    json_controller = pytest.json_controller
    response_overview = json_controller.get_response_overview()
    response_overview.update({"test": "ok"})
    assert json_controller.get_response_overview() != response_overview
    assert isinstance(json_controller.get_response_overview(), dict)


def test_get_overview():
    json_controller = pytest.json_controller
    overview = json_controller.get_overview()
    overview.update({"test": "ok"})
    assert json_controller.get_overview() != overview
    assert isinstance(json_controller.get_overview(), dict)


def test_to_list():
    json_controller = pytest.json_controller
    new_list = json_controller._to_list({
        "element1": {
            "field1": "value1",
            "field2": "value2"
        },
        "element2": {
            "field1": "value1",
            "field2": "value2"
        }
    }, "name")
    assert new_list == [{
        "field1": "value1",
        "field2": "value2",
        "name": "element2"
    }, {
        "field1": "value1",
        "field2": "value2",
        "name": "element1"
    }]


def test_error_when_execute_to_list_passing_invalid_params():
    json_controller = pytest.json_controller
    with pytest.raises(TypeError):
        json_controller._to_list(["a", "b", "c"])
