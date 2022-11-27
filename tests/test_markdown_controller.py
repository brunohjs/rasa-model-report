import os.path

import pytest
import responses

from src.rasa_model_report.controllers.JsonController import JsonController


def test_init_markdown_controller(rasa_path):
    markdown_controller = pytest.markdown_controller
    assert markdown_controller.project == "test-project"
    assert markdown_controller.version == "0.0.0"
    assert markdown_controller.RASA_PATH == rasa_path
    assert markdown_controller.OUTPUT_DIR == "./tests"
    assert markdown_controller.NLU_PATH == f"{rasa_path}/data"
    assert markdown_controller.RESULTS_PATH == f"{rasa_path}/results"
    assert markdown_controller.CONFIG_REPORT == f"{rasa_path}/config.yml"
    assert markdown_controller.OUTPUT_REPORT_FILE == f"{markdown_controller.OUTPUT_DIR}/model_report.md"
    assert markdown_controller.README_PATH == "README.md"
    assert isinstance(markdown_controller.json, object)
    assert isinstance(markdown_controller.csv, object)
    assert isinstance(markdown_controller.nlu, object)


def test_add_text():
    text_1 = "blablabla"
    text_2 = "another text"
    markdown_controller = pytest.markdown_controller
    markdown_controller.add_text(text_1)
    markdown_controller.add_text(["text", "in list"])
    markdown_controller.add_text(None)
    markdown_controller.add_text(text_2)
    assert markdown_controller.result == f"\n{text_1}\n{text_2}"


def test_add_image():
    path_to_image = "intent_confusion_matrix.png"
    markdown_controller = pytest.markdown_controller
    markdown_controller.add_image(path_to_image, "Title")
    assert os.path.isfile(f"{markdown_controller.RESULTS_PATH}/{path_to_image}")


def test_add_image_that_doesnt_exist():
    path_to_image = "image_that_doesnt_exist.png"
    markdown_controller = pytest.markdown_controller
    markdown_controller.add_image(path_to_image, "Title")
    assert not os.path.isfile(f"{markdown_controller.RESULTS_PATH}/{path_to_image}")


def test_break_line():
    text_1 = "blablabla"
    markdown_controller = pytest.markdown_controller
    markdown_controller.add_text(text_1)
    assert markdown_controller.result == f"\n{text_1}"
    markdown_controller.break_line()
    assert markdown_controller.result == f"\n{text_1}\n"


def test_build_table():
    markdown_controller = pytest.markdown_controller
    table = markdown_controller.build_table([["header_1", "header_2"], ["l1_c1", "l1_c2"], ["l2_c1", "l2_c2"]])
    assert isinstance(table, str)
    assert table == "|header_1|header_2|\n|-|-|\n|l1_c1|l1_c2|\n|l2_c1|l2_c2|\n"


def test_build_summary():
    markdown_controller = pytest.markdown_controller
    markdown_controller.nlu = pytest.nlu_controller
    text = markdown_controller.build_summary()
    assert isinstance(text, str)
    assert markdown_controller.nlu.is_connected() is True
    assert "#nlu" in text


def test_build_summary_without_nlu_section():
    markdown_controller = pytest.markdown_controller
    text = markdown_controller.build_summary()
    assert isinstance(text, str)
    assert markdown_controller.nlu.is_connected() is False
    assert "#nlu" not in text


def test_build_summary_without_config_section():
    markdown_controller = pytest.markdown_controller
    markdown_controller.CONFIG_REPORT = "path/of/invalid/file"
    text = markdown_controller.build_summary()
    assert isinstance(text, str)
    assert os.path.isfile(markdown_controller.CONFIG_REPORT) is False
    assert "#config" not in text


def test_build_overview():
    markdown_controller = pytest.markdown_controller
    text = markdown_controller.build_overview()
    assert isinstance(text, str)
    assert "## Overview" in text


def test_build_intent_title():
    markdown_controller = pytest.markdown_controller
    text = markdown_controller.build_intent_title()
    assert isinstance(text, str)
    assert "## Intenções <a name='intents'></a>" in text


def test_build_intent_overview():
    markdown_controller = pytest.markdown_controller
    text = markdown_controller.build_intent_overview()
    assert isinstance(text, str)


def test_build_intent_table():
    markdown_controller = pytest.markdown_controller
    text = markdown_controller.build_intent_table()
    assert isinstance(text, str)
    assert os.path.isfile(f"{markdown_controller.RESULTS_PATH}/intent_report.csv")


def test_build_intent_table_if_len_less_than_2():
    markdown_controller = pytest.markdown_controller
    json_controller = JsonController("invelid/path", "./", "test-project", "0.0.0")
    markdown_controller.json = json_controller
    text = markdown_controller.build_intent_table()
    assert isinstance(text, str)
    assert "Não foram encontradas" in text
    assert not os.path.isfile(f"{markdown_controller.RESULTS_PATH}/intent_report.csv")


def test_build_intent_errors_table():
    markdown_controller = pytest.markdown_controller
    text = markdown_controller.build_intent_errors_table()
    assert isinstance(text, str)
    assert os.path.isfile(f"{markdown_controller.RESULTS_PATH}/intent_errors.csv")


def test_build_intent_errors_table_if_len_less_than_2():
    markdown_controller = pytest.markdown_controller
    json_controller = JsonController("invelid/path", "./", "test-project", "0.0.0")
    markdown_controller.json = json_controller
    text = markdown_controller.build_intent_errors_table()
    assert isinstance(text, str)
    assert "Não foram encontradas" in text
    assert not os.path.isfile(f"{markdown_controller.RESULTS_PATH}/intent_errors.csv")


def test_build_entity_title():
    markdown_controller = pytest.markdown_controller
    text = markdown_controller.build_entity_title()
    assert isinstance(text, str)
    assert "## Entidades <a name='entities'></a>" in text


def test_build_entity_overview():
    markdown_controller = pytest.markdown_controller
    text = markdown_controller.build_entity_overview()
    assert isinstance(text, str)


def test_build_entity_table():
    markdown_controller = pytest.markdown_controller
    text = markdown_controller.build_entity_table()
    assert isinstance(text, str)
    assert os.path.isfile(f"{markdown_controller.RESULTS_PATH}/DIETClassifier_report.csv")


def test_build_entity_table_if_len_less_than_2():
    markdown_controller = pytest.markdown_controller
    json_controller = JsonController("invelid/path", "./", "test-project", "0.0.0")
    markdown_controller.json = json_controller
    text = markdown_controller.build_entity_table()
    assert isinstance(text, str)
    assert "Não foram encontradas" in text
    assert not os.path.isfile(f"{markdown_controller.RESULTS_PATH}/DIETClassifier_report.csv")


def test_build_entity_errors_table():
    markdown_controller = pytest.markdown_controller
    text = markdown_controller.build_entity_errors_table()
    assert isinstance(text, str)


def test_build_entity_errors_table_if_len_less_than_2():
    markdown_controller = pytest.markdown_controller
    json_controller = JsonController("invelid/path", "./", "test-project", "0.0.0")
    markdown_controller.json = json_controller
    text = markdown_controller.build_entity_errors_table()
    assert isinstance(text, str)
    assert "Não foram encontradas" in text


def test_build_response_title():
    markdown_controller = pytest.markdown_controller
    text = markdown_controller.build_response_title()
    assert isinstance(text, str)
    assert "## Respostas <a name='responses'></a>" in text


def test_build_response_overview():
    markdown_controller = pytest.markdown_controller
    text = markdown_controller.build_response_overview()
    assert isinstance(text, str)


def test_build_response_table():
    markdown_controller = pytest.markdown_controller
    text = markdown_controller.build_response_table()
    assert isinstance(text, str)
    assert os.path.isfile(f"{markdown_controller.RESULTS_PATH}/story_report.csv")


def test_build_response_table_if_len_less_than_2():
    markdown_controller = pytest.markdown_controller
    json_controller = JsonController("invelid/path", "./", "test-project", "0.0.0")
    markdown_controller.json = json_controller
    text = markdown_controller.build_response_table()
    assert isinstance(text, str)
    assert "Não foram encontradas" in text
    assert not os.path.isfile(f"{markdown_controller.RESULTS_PATH}/story_report.csv")


def test_build_nlu_title():
    markdown_controller = pytest.markdown_controller
    text = markdown_controller.build_nlu_title()
    assert isinstance(text, str)
    assert "## NLU <a name='nlu'></a>" in text


@responses.activate
def test_build_nlu_table():
    markdown_controller = pytest.markdown_controller
    markdown_controller.nlu = pytest.nlu_controller
    text = markdown_controller.build_nlu_table()
    assert isinstance(text, str)
    assert os.path.isfile(f"{markdown_controller.RESULTS_PATH}/nlu_report.csv")


def test_build_nlu_table_if_len_less_than_2():
    markdown_controller = pytest.markdown_controller
    json_controller = JsonController("invelid/path", "./", "test-project", "0.0.0")
    markdown_controller.json = json_controller
    text = markdown_controller.build_nlu_table()
    assert isinstance(text, str)
    assert "Não foram encontradas" in text
    assert not os.path.isfile(f"{markdown_controller.RESULTS_PATH}/nlu_report.csv")


def test_build_nlu_errors_table():
    markdown_controller = pytest.markdown_controller
    markdown_controller.nlu._problem_sentences.append({
        "intent": "test",
        "text": "test",
        "understood": False,
        "confidence": 0.7,
        "predicted_intent": "nlu_fallback"
    })
    text = markdown_controller.build_nlu_errors_table()
    assert isinstance(text, str)


def test_build_nlu_errors_table_if_len_less_than_2():
    markdown_controller = pytest.markdown_controller
    json_controller = JsonController("invalid/path", "./", "test-project", "0.0.0")
    markdown_controller.json = json_controller
    text = markdown_controller.build_nlu_errors_table()
    assert isinstance(text, str)
    assert "Não há sentenças" in text


def test_build_config_report():
    markdown_controller = pytest.markdown_controller
    text = markdown_controller.build_config_report()
    assert isinstance(text, str)
    assert "## Configurações <a name='configs'></a>" in text


def test_dont_build_config_report_when_there_is_no_config_file():
    markdown_controller = pytest.markdown_controller
    markdown_controller.CONFIG_REPORT = "path/of/invalid/file"
    text = markdown_controller.build_config_report()
    assert isinstance(text, str)
    assert not text


def test_save_report():
    markdown_controller = pytest.markdown_controller
    markdown_controller.save_report()
    # Save again to cover the "file changed" message line
    markdown_controller.save_report()
    assert os.path.isfile(markdown_controller.OUTPUT_REPORT_FILE)


def test_save_overview():
    markdown_controller = pytest.markdown_controller
    markdown_controller.save_overview()
    assert os.path.isfile(markdown_controller.json.OVERVIEW_REPORT)


def test_build_line_entity_when_there_is_no_entities():
    markdown_controller = pytest.markdown_controller
    text = markdown_controller.build_line_entity([])
    assert text == "-"


def test_build_line_table():
    markdown_controller = pytest.markdown_controller
    text = markdown_controller._build_line_table({
        "name": "test-name",
        "f1-score": 1,
        "precision": 0.8,
        "support": 0.9,
        "recall": 0.9
    })
    assert text == ["🟢", "test-name", "80.0%", "90.0%", "100.0%", "0.9"]
