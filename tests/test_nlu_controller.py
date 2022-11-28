from unittest import mock

import pytest
import requests.exceptions
import responses

from src.rasa_model_report.controllers.nlu_controller import NluController
from tests import utils


@pytest.fixture(autouse=True)
def execute_before_each_test(rasa_path):
    load_controllers(rasa_path)
    pytest.file_name = "test.csv"
    yield
    utils.remove_generated_files(rasa_path)


@responses.activate
def load_controllers(rasa_path):
    output_path = "./tests"
    project_name = "test-project"
    version = "0.0.0"
    utils.load_mock_payloads()
    nlu_controller = NluController(rasa_path, output_path, project_name, version)
    pytest.nlu_controller = nlu_controller


def test_init_nlu_controller(rasa_path):
    nlu_controller = pytest.nlu_controller
    assert nlu_controller.project == "test-project"
    assert nlu_controller.version == "0.0.0"
    assert nlu_controller.rasa_path == rasa_path
    assert nlu_controller.output_path == "./tests"
    assert nlu_controller.nlu_path == f"{rasa_path}/data"
    assert nlu_controller.results_path == f"{rasa_path}/results"
    assert nlu_controller.config_report_path == f"{rasa_path}/config.yml"
    assert nlu_controller.is_connected() is True


def test_init_nlu_controller_when_no_rasa():
    nlu_controller = pytest.nlu_controller
    assert nlu_controller.is_connected() is False


def test_get_data():
    nlu_controller = pytest.nlu_controller
    data = nlu_controller.get_data()
    data.append({"test": "ok"})
    assert nlu_controller.get_data() != data
    assert isinstance(nlu_controller.get_data(), list)


def test_get_problem_sentences():
    nlu_controller = pytest.nlu_controller
    sentences = nlu_controller.get_problem_sentences()
    sentences.append({"test": "ok"})
    assert nlu_controller.get_problem_sentences() != sentences
    assert isinstance(nlu_controller.get_problem_sentences(), list)


def test_get_general_grade():
    nlu_controller = pytest.nlu_controller
    nlu_controller._calculate_general_grade()
    assert nlu_controller.get_general_grade() >= 0
    assert isinstance(nlu_controller.get_general_grade(), float)


@responses.activate
def test_request_nlu():
    utils.load_mock_payloads()
    nlu_controller = pytest.nlu_controller
    data = nlu_controller.request_nlu("test")
    assert isinstance(data, dict)
    assert isinstance(data.get("text"), str)
    assert isinstance(data.get("intent"), dict)
    assert isinstance(data.get("entities"), list)
    assert isinstance(data.get("intent_ranking"), list)


@responses.activate
def test_request_nlu_error():
    utils.load_mock_payloads()
    nlu_controller = pytest.nlu_controller
    data = nlu_controller.request_nlu("test")
    assert data == {}


def test_remove_entities_from_text():
    nlu_controller = pytest.nlu_controller
    tests_texts = {
        "entity test [blue](color) and [red](color).": "entity test blue and red.",
        "[orange]{\"entity\": \"color\", \"value\": \"Orange\"} is an amazing color.": "orange is an amazing color.",
        "": "",
        " ": " ",
        "text that doesn't exist entity": "text that doesn't exist entity",
        "text with (parentheses)": "text with (parentheses)"
    }
    for test_text, expected in tests_texts.items():
        assert nlu_controller.remove_entities_from_text(test_text) == expected


def test_select_normal_intent():
    nlu_controller = pytest.nlu_controller
    payload = {
        "text": "oi",
        "intent": {
            "id": 6130133147372115834,
            "name": "greet",
            "confidence": 0.77470862865448
        },
        "entities": [],
        "intent_ranking": [
            {
                "id": 6130133147372115834,
                "name": "greet",
                "confidence": 0.77470862865448
            },
            {
                "id": 684865172093367490,
                "name": "affirm",
                "confidence": 0.15055057406425476
            }
        ]
    }
    assert nlu_controller.select_intent(payload) == payload.get("intent")


def test_select_nlu_fallback_intent():
    nlu_controller = pytest.nlu_controller
    payload = {
        "text": "oi",
        "intent": {
            "id": 6136533147372685482,
            "name": "nlu_fallback",
            "confidence": 0.8
        },
        "entities": [],
        "intent_ranking": [
            {
                "id": 6136533147372685482,
                "name": "nlu_fallback",
                "confidence": 0.8
            },
            {
                "id": 6130133147372115834,
                "name": "greet",
                "confidence": 0.77470862865448
            }
        ]
    }
    result = payload["intent_ranking"][1]
    result["nlu_fallback"] = True
    assert nlu_controller.select_intent(payload) == result


@responses.activate
def test_request_rasa_api_200():
    utils.load_mock_payloads()
    nlu_controller = pytest.nlu_controller
    response = nlu_controller.request_rasa_api("http://localhost:5005")
    assert response.status_code == 200


@responses.activate
def test_request_rasa_api_general_error():
    utils.load_mock_payloads()
    nlu_controller = pytest.nlu_controller
    response = nlu_controller.request_rasa_api("invalid url")
    assert response is None


@responses.activate
def test_request_rasa_api_connection_error():
    nlu_controller = pytest.nlu_controller
    with mock.patch("requests.get", side_effect=requests.exceptions.ConnectionError()):
        response = nlu_controller.request_rasa_api("http://localhost:5005")
        assert response is None
