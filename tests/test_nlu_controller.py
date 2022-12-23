import pytest
import responses

from rasa_model_report.controllers.nlu_controller import NluController
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
    project_version = "0.0.0"
    utils.load_mock_payloads()
    nlu_controller = NluController(rasa_path, output_path, project_name, project_version)
    pytest.nlu_controller = nlu_controller


def test_init_nlu_controller(rasa_path):
    nlu_controller = pytest.nlu_controller
    assert nlu_controller.project_name == "test-project"
    assert nlu_controller.project_version == "0.0.0"
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
    data = nlu_controller.data
    data.append({"test": "ok"})
    assert nlu_controller.data != data
    assert isinstance(nlu_controller.data, list)


def test_get_problem_sentences():
    nlu_controller = pytest.nlu_controller
    sentences = nlu_controller.problem_sentences
    sentences.append({"test": "ok"})
    assert nlu_controller.problem_sentences != sentences
    assert isinstance(nlu_controller.problem_sentences, list)


def test_get_general_grade():
    nlu_controller = pytest.nlu_controller
    nlu_controller._calculate_general_grade()
    assert nlu_controller.general_grade >= 0
    assert isinstance(nlu_controller.general_grade, float)


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
    result = {
        "id": 6130133147372115834,
        "name": "greet",
        "confidence": 0.77470862865448,
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
    assert nlu_controller.select_intent(payload) == result


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
    result = {
        "id": 6130133147372115834,
        "name": "greet",
        "confidence": 0.77470862865448,
        "nlu_fallback": True,
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
    assert nlu_controller.select_intent(payload) == result


def test_select_chitchat_intent():
    nlu_controller = pytest.nlu_controller
    payload = {
        "text": "What's up man",
        "intent": {
            "id": 2906457073168819123,
            "name": "chitchat",
            "confidence": 0.999968945980072
        },
        "entities": [],
        "intent_ranking": [
            {
                "id": 2906457073168819123,
                "name": "chitchat",
                "confidence": 0.999968945980072
            },
            {
                "id": 7260289726461652906,
                "name": "ask_which_events",
                "confidence": 1.3520077118300833e-05
            }
        ],
        "response_selector": {
            "all_retrieval_intents": [
                "chitchat"
            ],
            "chitchat": {
                "response": {
                    "id": 1089191035510850432,
                    "responses": [
                        {
                            "text": "I'm great! Thanks for asking."
                        }
                    ],
                    "response_templates": [
                        {
                            "text": "I'm great! Thanks for asking."
                        }
                    ],
                    "confidence": 0.9999934434890747,
                    "intent_response_key": "chitchat/ask_howdoing",
                    "utter_action": "utter_chitchat/ask_howdoing",
                    "template_name": "utter_chitchat/ask_howdoing"
                },
                "ranking": [
                    {
                        "id": 1089191035510850432,
                        "confidence": 0.9999934434890747,
                        "intent_response_key": "chitchat/ask_howdoing"
                    },
                    {
                        "id": 1401854538324391268,
                        "confidence": 4.242805516696535e-06,
                        "intent_response_key": "chitchat/ask_whatisrasa"
                    }
                ]
            }
        }
    }
    result = {
        "id": 1089191035510850432,
        "confidence": 0.9999934434890747,
        "name": "chitchat/ask_howdoing",
        "intent_ranking": [{
            "id": 1089191035510850432,
            "confidence": 0.9999934434890747,
            "name": "chitchat/ask_howdoing"
        },
            {
            "id": 1401854538324391268,
            "confidence": 4.242805516696535e-06,
            "name": "chitchat/ask_whatisrasa"
        }]
    }
    assert nlu_controller.select_intent(payload) == result
