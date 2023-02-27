import os

import pytest

from rasa_model_report.controllers.e2e_coverage_controller import E2ECoverageController
from tests import utils


@pytest.fixture(autouse=True)
def execute_before_each_test(rasa_path):
    output_path = "./tests"
    actions_path = None
    project_name = "test-project"
    project_version = "0.0.0"
    e2e_coverage_controller = E2ECoverageController(rasa_path, output_path, actions_path, project_name, project_version)
    pytest.e2e_coverage_controller = e2e_coverage_controller
    yield
    utils.remove_generated_files(rasa_path)


def test_init_e2e_coverage_controller(rasa_path):
    e2e_coverage_controller = pytest.e2e_coverage_controller
    assert e2e_coverage_controller.project_name == "test-project"
    assert e2e_coverage_controller.project_version == "0.0.0"
    assert e2e_coverage_controller.rasa_path == rasa_path
    assert e2e_coverage_controller.output_path == "./tests"
    assert e2e_coverage_controller.nlu_path == f"{rasa_path}/data"
    assert e2e_coverage_controller.results_path == f"{rasa_path}/results"
    assert e2e_coverage_controller.config_report_path == f"{rasa_path}/config.yml"


def test_load_domain_elements():
    e2e_coverage_controller = pytest.e2e_coverage_controller
    e2e_coverage_controller._load_domain_elements()

    # Check if _actions is a list
    assert isinstance(e2e_coverage_controller._actions, list)

    # Check if each _actions element is a string
    assert all(isinstance(item, str) for item in e2e_coverage_controller._actions)

    # Check if _actions have elements
    assert len(e2e_coverage_controller._actions) > 0

    # Check if _intents is a list
    assert isinstance(e2e_coverage_controller._intents, list)

    # Check if each _intents element is a string
    assert all(isinstance(item, str) for item in e2e_coverage_controller._intents)

    # Check if _intents have elements
    assert len(e2e_coverage_controller._actions) > 0

    # Check if _entities is a list
    assert isinstance(e2e_coverage_controller._entities, list)

    # Check if each _entities element is a string
    assert all(isinstance(item, str) for item in e2e_coverage_controller._entities)

    # Check if _entities have elements
    assert len(e2e_coverage_controller._actions) > 0


def test_generate_e2e_report_string():
    e2e_coverage_controller = pytest.e2e_coverage_controller
    e2e_coverage_controller._generate()
    assert e2e_coverage_controller._total_num_elements >= 0
    assert e2e_coverage_controller._total_num_not_covered >= 0
    assert e2e_coverage_controller._total_rate >= 0


def test_save_e2e_report_when_have_not_covered_items():
    e2e_coverage_controller = pytest.e2e_coverage_controller
    e2e_coverage_controller.save()
    assert os.path.isfile(f"{e2e_coverage_controller.results_path}/e2e_coverage_report.txt")


def test_dont_save_e2e_report_when_havent_items():
    e2e_coverage_controller = pytest.e2e_coverage_controller
    file_path = f"{e2e_coverage_controller.results_path}/e2e_coverage_report.txt"
    if os.path.isfile(file_path):
        os.remove(file_path)
    e2e_coverage_controller._total_num_not_covered = 0
    e2e_coverage_controller.save()
    assert not os.path.isfile(file_path)


def test_have_not_covered_items():
    e2e_coverage_controller = pytest.e2e_coverage_controller
    assert e2e_coverage_controller.have_not_covered_items() is True


def test_havent_not_covered_items():
    e2e_coverage_controller = pytest.e2e_coverage_controller
    e2e_coverage_controller._total_num_not_covered = 0
    assert e2e_coverage_controller.have_not_covered_items() is False


def test_e2e_coverage_get_data():
    e2e_coverage_controller = pytest.e2e_coverage_controller
    data = e2e_coverage_controller.data
    data.update({"test": ["test1", "test2", "test3"]})
    assert e2e_coverage_controller.data != data
    assert isinstance(e2e_coverage_controller.data, dict)


def test_e2e_coverage_get_total_rate():
    e2e_coverage_controller = pytest.e2e_coverage_controller
    total_rate = e2e_coverage_controller.total_rate
    total_rate += 1
    assert e2e_coverage_controller.total_rate != total_rate
    assert isinstance(e2e_coverage_controller.total_rate, float)


def test_e2e_coverage_get_total_num_elements():
    e2e_coverage_controller = pytest.e2e_coverage_controller
    total_num_elements = e2e_coverage_controller.total_num_elements
    total_num_elements += 1
    assert e2e_coverage_controller.total_num_elements != total_num_elements
    assert isinstance(e2e_coverage_controller.total_num_elements, int)


def test_e2e_coverage_get_total_num_not_covered():
    e2e_coverage_controller = pytest.e2e_coverage_controller
    total_num_not_covered = e2e_coverage_controller.total_num_not_covered
    total_num_not_covered += 1
    assert e2e_coverage_controller.total_num_not_covered != total_num_not_covered
    assert isinstance(e2e_coverage_controller.total_num_not_covered, int)


def test_e2e_coverage_exclude_special_actions():
    e2e_coverage_controller = pytest.e2e_coverage_controller
    e2e_coverage_controller._actions.extend([
        "utter_ask_test_slot",
        "validate_slot_form",
        "action_ask_slot",
        "action_correct",
        "utter_ok"
    ])
    actions = e2e_coverage_controller._exclude_special_actions()
    assert "utter_ask_test_slot" not in actions
    assert "validate_slot_form" not in actions
    assert "action_ask_slot" not in actions
    assert "action_correct" in actions
    assert "utter_ok" in actions


def test_e2e_coverage_get_utters_in_actions(rasa_path):
    e2e_coverage_controller = pytest.e2e_coverage_controller
    utters = e2e_coverage_controller.get_utters_in_actions()
    assert len(utters) == 4
    assert "utter_test" in utters
    assert "action_test" in utters
    assert "action_test2" in utters
    assert "action_test3" in utters
    assert "validate_slot" not in utters
