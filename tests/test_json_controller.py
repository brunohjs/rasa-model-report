import os.path
import random

import pytest

from rasa_model_report.controllers.json_controller import JsonController
from tests import utils


@pytest.fixture(autouse=True)
def execute_before_each_test(rasa_path):
    output_path = "./tests"
    project_name = "test-project"
    project_version = "0.0.0"
    json_controller = JsonController(rasa_path, output_path, project_name, project_version)
    pytest.json_controller = json_controller
    yield
    utils.remove_generated_files(rasa_path)


def test_init_json_controller(rasa_path):
    json_controller = pytest.json_controller
    assert json_controller.project_name == "test-project"
    assert json_controller.project_version == "0.0.0"
    assert json_controller.rasa_path == rasa_path
    assert json_controller.output_path == "./tests"
    assert json_controller.nlu_path == f"{rasa_path}/data"
    assert json_controller.results_path == f"{rasa_path}/results"
    assert json_controller.config_report_path == f"{rasa_path}/config.yml"
    assert json_controller.intent_report_path == f"{json_controller.results_path}/intent_report.json"
    assert json_controller.intent_errors_path == f"{json_controller.results_path}/intent_errors.json"
    assert json_controller.entity_report_path == f"{json_controller.results_path}/DIETClassifier_report.json"
    assert json_controller.entity_errors_path == f"{json_controller.results_path}/DIETClassifier_errors.json"
    assert json_controller.story_report_path == f"{json_controller.results_path}/story_report.json"
    assert json_controller.overview_report_path == f"{json_controller.results_path}/overview.json"


def test_load_json_file():
    json_controller = pytest.json_controller
    data = json_controller.load_json_file(json_controller.intent_report_path)
    assert isinstance(data, dict)


def test_load_json_file_but_a_non_existent_file():
    json_controller = pytest.json_controller
    with pytest.raises(Exception):
        json_controller.load_json_file("path/that/does/not/exist.json")
        json_controller.load_json_file("path/that/does/not/exist.json", "warning")


def test_load_intents():
    json_controller = pytest.json_controller
    json_controller._load_intents()
    assert isinstance(json_controller.intents, list)
    assert len(json_controller.intents) > 0


def test_load_intents_but_a_non_existent_file():
    json_controller = pytest.json_controller
    json_controller.intent_report_path = "path/that/does/not/exist.json"
    json_controller._load_intents()
    assert json_controller.intents == []


def test_load_entities():
    json_controller = pytest.json_controller
    json_controller._load_entities()
    assert isinstance(json_controller.entities, list)
    assert len(json_controller.entities) > 0


def test_load_entities_but_a_non_existent_file():
    json_controller = pytest.json_controller
    json_controller.entity_report_path = "path/that/does/not/exist.json"
    json_controller._load_entities()
    assert json_controller.entities == []


def test_load_overview():
    json_controller = pytest.json_controller
    json_controller._load_overview()
    overview = json_controller.overview
    assert isinstance(overview, dict)
    assert isinstance(overview.get("project"), str)
    assert isinstance(overview.get("version"), str)
    assert isinstance(overview.get("updated_at"), str)
    assert isinstance(overview.get("intent"), float)
    assert isinstance(overview.get("entity"), float)
    assert isinstance(overview.get("core"), float)
    assert isinstance(overview.get("nlu"), float) or overview.get("nlu") is None
    assert isinstance(overview.get("e2e_coverage"), float) or overview.get("e2e_coverage") is None
    assert isinstance(overview.get("overall"), float)
    assert isinstance(overview.get("created_at"), str)


def test_load_overview_if_exists():
    json_controller = pytest.json_controller
    json_controller._load_overview()
    json_controller.save_overview()
    json_controller._load_overview()
    assert isinstance(json_controller.overview, dict)


def test_save_overview():
    json_controller = pytest.json_controller
    json_controller.save_overview()
    assert os.path.isfile(json_controller.overview_report_path)


def test_calculate_overall():
    json_controller = pytest.json_controller
    json_controller._calculate_overall()
    assert isinstance(json_controller.overview.get("overall"), float)


def test_update_overview():
    json_controller = pytest.json_controller
    random_number = random.randint(0, 100)
    json_controller.update_overview({
        "nlu": random_number
    })
    assert json_controller.overview.get("nlu") == random_number


def test_dont_update_overview_when_not_a_dict_as_a_param():
    json_controller = pytest.json_controller
    overview = json_controller.overview
    json_controller.update_overview(["test", "5"])
    assert json_controller.overview == overview


def test_get_intents():
    json_controller = pytest.json_controller
    intents = json_controller.intents
    intents.append({"test": "ok"})
    assert json_controller.intents != intents
    assert isinstance(json_controller.intents, list)


def test_get_intent_overview():
    json_controller = pytest.json_controller
    intent_overview = json_controller.intent_overview
    intent_overview.update({"test": "ok"})
    assert json_controller.intent_overview != intent_overview
    assert isinstance(json_controller.intent_overview, dict)


def test_get_intent_errors():
    json_controller = pytest.json_controller
    intents = json_controller.intent_errors
    intents.append({"test": "ok"})
    assert json_controller.intent_errors != intents
    assert isinstance(json_controller.intent_errors, list)


def test_get_entities():
    json_controller = pytest.json_controller
    entities = json_controller.entities
    entities.append({"test": "ok"})
    assert json_controller.entities != entities
    assert isinstance(json_controller.entities, list)


def test_get_entity_overview():
    json_controller = pytest.json_controller
    entity_overview = json_controller.entity_overview
    entity_overview.update({"test": "ok"})
    assert json_controller.entity_overview != entity_overview
    assert isinstance(json_controller.entity_overview, dict)


def test_get_entity_errors():
    json_controller = pytest.json_controller
    entities = json_controller.entity_errors
    entities.append({"test": "ok"})
    assert json_controller.entity_errors != entities
    assert isinstance(json_controller.entity_errors, list)


def test_get_core():
    json_controller = pytest.json_controller
    core = json_controller.core
    core.append({"test": "ok"})
    assert json_controller.core != core
    assert isinstance(json_controller.core, list)


def test_get_core_overview():
    json_controller = pytest.json_controller
    core_overview = json_controller.core_overview
    core_overview.update({"test": "ok"})
    assert json_controller.core_overview != core_overview
    assert isinstance(json_controller.core_overview, dict)


def test_get_overview():
    json_controller = pytest.json_controller
    overview = json_controller.overview
    overview.update({"test": "ok"})
    assert json_controller.overview != overview
    assert isinstance(json_controller.overview, dict)


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


def test_extract_entity_from_string():
    json_controller = pytest.json_controller
    assert json_controller.extract_entity_from_string(
        "[depósito]{\"entity\": \"meio_pagamento\", \"value\": \"deposito\"}"
    ) == "meio_pagamento"
    assert json_controller.extract_entity_from_string(
        "[débito automático]{\"entity\": \"meio_pagamento\", \"value\": \"debito automatico\"}"
    ) == "meio_pagamento"
    assert json_controller.extract_entity_from_string(
        "[transferências]{\"entity\": \"tipo_operacao\", \"value\": \"transferencia\"}"
    ) == "tipo_operacao"
    assert json_controller.extract_entity_from_string(
        "[saldo](meio_pagamento)"
    ) == "meio_pagamento"
    assert json_controller.extract_entity_from_string(
        "[bo20](erros_outros)"
    ) == "erros_outros"
    assert json_controller.extract_entity_from_string("utter_without_entity_test") == "utter_without_entity_test"
    with pytest.raises(TypeError):
        json_controller.extract_entity_from_string()
