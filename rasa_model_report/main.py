import logging

import click

from rasa_model_report.controllers.model_report import ModelReport

logging.basicConfig(format="%(asctime)s [%(levelname)s] %(message)s", level=logging.INFO)


@click.command()
@click.option(
    "--disable-nlu",
    is_flag=True,
    required=False,
    default=False,
    help="Disable processing NLU sentences. NLU section will not be generated "
    "in the report. Required Rasa API. (default: false)"
)
@click.help_option(
    "--help",
    "-h",
    help="Show this help message."
)
@click.option(
    "--model-link",
    type=str,
    required=False,
    help="Model download link. It's only displayed in the report to model download."
)
@click.option(
    "--output-path",
    type=str,
    required=False,
    default="./",
    help="Report output path. (default: ./)"
)
@click.option(
    "--path",
    "-p",
    type=str,
    required=False,
    default="./",
    help="Rasa project path. (default: ./)"
)
@click.option(
    "--project-name",
    type=str,
    required=False,
    default="My Project",
    help="Rasa project name. It's only displayed in the report. (default: My project)"
)
@click.option(
    "--project-version",
    type=str,
    required=False,
    default=None,
    help="Project version. It's only displayed in the report for project documentation."
)
@click.option(
    "--rasa-api",
    type=str,
    required=False,
    default="http://localhost:5005",
    help="Rasa API URL. Is needed to create NLU section of report. (default: http://localhost:5005)"
)
@click.option(
    "--rasa-version",
    type=str,
    required=False,
    default=None,
    help="Rasa version. It's only displayed in the report for project documentation."
)
@click.version_option(
    None,
    "--version",
    "-v",
    message="v%(version)s",
    help="Show installed rasa-model-report version.",
)
def main(disable_nlu, model_link, output_path, path, project_name, project_version, rasa_api, rasa_version):
    """
    Simple add-on that generates training model health reports for your Rasa projects. 📈🔍🧾🤖🧠
    """
    report = ModelReport(
        path,
        output_path,
        project_name,
        rasa_version,
        project_version,
        disable_nlu=disable_nlu,
        rasa_api_url=rasa_api,
        model_link=model_link
    )
    return report
