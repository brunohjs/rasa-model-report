import logging

import click

from rasa_model_report.controllers.model_report import ModelReport
from rasa_model_report.helpers import constants

logging.basicConfig(format="%(asctime)s [%(levelname)s] %(message)s", level=logging.INFO)
for name in logging.root.manager.loggerDict:
    logging.getLogger(name).propagate = False


@click.command()
@click.option(
    "--actions-path",
    required=False,
    show_default=True,
    help="Actions path. [default: actions/ inside Rasa project path]"
)
@click.option(
    "--disable-nlu",
    is_flag=True,
    required=False,
    default=constants.DISABLE_NLU,
    show_default=True,
    help="Disable processing NLU sentences. NLU section will not be generated "
    "in the report. Required Rasa API."
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
    show_default=True,
    help="Model download link. It's only displayed in the report to model download."
)
@click.option(
    "--no-images",
    is_flag=True,
    required=False,
    default=constants.NO_IMAGES,
    show_default=True,
    help="Generate model report without images."
)
@click.option(
    "--output-format",
    type=click.Choice(["md", "pdf"], case_sensitive=False),
    required=False,
    default=constants.OUTPUT_FORMAT,
    show_default=True,
    help="Model report format."
)
@click.option(
    "--output-path",
    type=str,
    required=False,
    default=constants.OUTPUT_PATH,
    show_default=True,
    help="Report output path."
)
@click.option(
    "--path",
    "-p",
    type=str,
    required=False,
    default=constants.RASA_PATH,
    show_default=True,
    help="Rasa project path."
)
@click.option(
    "--precision",
    type=click.IntRange(0, 5),
    required=False,
    default=constants.GRADE_PRECISION,
    show_default=True,
    help="Grade precision. Used to change precision of the model report overview grades. "
    "Can vary between 0 and 5."
)
@click.option(
    "--project-name",
    type=str,
    required=False,
    default=constants.PROJECT_NAME,
    show_default=True,
    help="Rasa project name. It's only displayed in the report."
)
@click.option(
    "--project-version",
    type=str,
    required=False,
    default=constants.PROJECT_VERSION,
    show_default=True,
    help="Project version. It's only displayed in the report for project documentation."
)
@click.option(
    "--rasa-api",
    type=str,
    required=False,
    default=constants.RASA_API_URL,
    show_default=True,
    help="Rasa API URL. Is needed to create NLU section of report."
)
@click.option(
    "--rasa-version",
    type=str,
    required=False,
    default=constants.RASA_VERSION,
    show_default=True,
    help="Rasa version. It's only displayed in the report for project documentation."
)
@click.version_option(
    None,
    "--version",
    "-v",
    message="v%(version)s",
    show_default=True,
    help="Show installed rasa-model-report version.",
)
def main(
    actions_path,
    disable_nlu,
    model_link,
    no_images,
    output_format,
    output_path,
    path,
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
        output_format=output_format,
        precision=precision
    )
    return report
