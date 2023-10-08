import logging

import click

from rasa_model_report.controllers.model_report import ModelReport
from rasa_model_report.helpers import constants

logging.basicConfig(format="%(asctime)s [%(levelname)s] %(message)s", level=logging.INFO)


@click.command()
@click.option(
    "--actions-path",
    required=False,
    help="Actions path. (default: actions/ inside Rasa project path)"
)
@click.option(
    "--disable-nlu",
    is_flag=True,
    required=False,
    default=constants.DISABLE_NLU,
    help="Disable processing NLU sentences. NLU section will not be generated "
    "in the report. Required Rasa API."
)
@click.option(
    "--exclude",
    "-e",
    required=False,
    multiple=True,
    help="List of utter and actions that will be exclude in the E2E test coverage. Use commas to separate items. "
    "Example: utter_greet,utter_goodbye,action_listen"
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
    "--no-images",
    is_flag=True,
    required=False,
    default=constants.NO_IMAGES,
    help="Generate model report without images."
)
@click.option(
    "--output-path",
    type=str,
    required=False,
    default=constants.OUTPUT_PATH,
    help=f"Report output path. (default: {constants.OUTPUT_PATH})"
)
@click.option(
    "--path",
    "-p",
    type=str,
    required=False,
    default=constants.RASA_PATH,
    help=f"Rasa project path. (default: {constants.RASA_PATH})"
)
@click.option(
    "--precision",
    type=int,
    required=False,
    default=constants.GRADE_PRECISION,
    help="Grade precision. Used to change precision of the model report overview grades. "
    f"Can vary between 0 and 5 (default: {constants.GRADE_PRECISION})"
)
@click.option(
    "--project-name",
    type=str,
    required=False,
    default=constants.PROJECT_NAME,
    help=f"Rasa project name. It's only displayed in the report. (default: {constants.PROJECT_NAME})"
)
@click.option(
    "--project-version",
    type=str,
    required=False,
    default=constants.PROJECT_VERSION,
    help="Project version. It's only displayed in the report for project documentation."
)
@click.option(
    "--rasa-api",
    type=str,
    required=False,
    default=constants.RASA_API_URL,
    help=f"Rasa API URL. Is needed to create NLU section of report. (default: {constants.RASA_API_URL})"
)
@click.option(
    "--rasa-version",
    type=str,
    required=False,
    default=constants.RASA_VERSION,
    help="Rasa version. It's only displayed in the report for project documentation."
)
@click.version_option(
    None,
    "--version",
    "-v",
    message="v%(version)s",
    help="Show installed rasa-model-report version.",
)
def main(
    actions_path,
    disable_nlu,
    exclude,
    model_link,
    no_images,
    output_path, path,
    precision,
    project_name,
    project_version,
    rasa_api,
    rasa_version
):
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
        model_link=model_link,
        actions_path=actions_path,
        no_images=no_images,
        precision=precision,
        exclude=[item for row in exclude for item in row.split(",")]
    )
    return report
