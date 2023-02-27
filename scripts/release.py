# This script is responsable for launching new app releases.
import json
import logging
import os.path
import re
import shutil
import subprocess
import sys
from typing import Optional


logging.basicConfig(format="%(asctime)s [%(levelname)s] %(message)s", level=logging.INFO)
MAIN_BRANCH = "main"


def close_milestone(version: str) -> None:
    """
    Close version milestone on Github.

    :param version: Version.
    """
    milestone = subprocess.run(["gh milestone list --json title,number"], shell=True, capture_output=True)
    milestone = {item["title"]: item["number"] for item in json.loads(milestone.stdout)}
    if version in milestone:
        subprocess.run([
            f"gh milestone edit {milestone[version]} -s closed"
        ])
        logging.info("")
    else:
        error_message = f"Milestone {version} not found."
        logging.error(error_message)
        raise Exception(error_message)


def get_changelog(version: str) -> Optional[str]:
    """
    Get version notes from changelog file.

    :param version: Version.
    :return: Version notes.
    """
    file = open("CHANGELOG.md")
    data = file.read()
    splitted_text = re.split(r"\n## ", data)
    for text in splitted_text:
        regex = r"\[" + version + r"\] - \d{4}-\d{2}-\d{2}\n"
        if re.match(regex, text):
            logging.info(f"Changelog notes found for version {version}.")
            return re.sub(regex, "", text).strip()
    else:
        error_message = f"No notes found for version {version}. Update CHANGELOG.md file."
        logging.error(error_message)
        raise Exception(error_message)


def create_release(version: str, notes: str) -> None:
    """
    Create release on Github.

    :param version: Tag version.
    :param notes: Release notes.
    """
    try:
        subprocess.run([
            f"gh release create {version} -R 'github.com/brunohjs/rasa-model-report' --verify-tag --notes '{notes}'"
        ], shell=True)
        logging.info("Release created on Github.")
    except Exception as error:
        logging.error(f"Could not create release. Error: {error}")


def update_version_setup_file(new_version: str) -> None:
    """
    Update version in setup.py file.

    :param new_version: New version.
    """
    file = open("setup.py")
    data = file.read()
    data = re.sub(r"version=\"\d+\.\d+\.\d+\",", f"version=\"{new_version}\",", data)
    file.close()
    file = open("setup.py", "w")
    file.write(data)
    file.close()


def get_new_version() -> str:
    """
    Get current version from Github tags and return new version.

    :return: New version.
    """
    logging.info("Getting last version")
    subprocess.run(["git", "fetch", "--all"], shell=False)
    versions = subprocess.check_output(["git", "tag"]).decode('ascii').strip().split('\n')
    version = versions[-1] if versions and versions[0] else '0.0.0'
    logging.info(f"Last version: v{version}")
    version = version.split('.')
    if len(sys.argv) > 1:
        if sys.argv[1] == "major":
            version[0] = str(int(version[0]) + 1)
            version[1] = "0"
            version[2] = "0"
        elif sys.argv[1] == "minor":
            version[1] = str(int(version[1]) + 1)
            version[2] = "0"
        elif sys.argv[1] == "patch":
            version[2] = str(int(version[2]) + 1)
        logging.info(f"New {sys.argv[1]} version")
    else:
        version[2] = str(int(version[2]) + 1)
        logging.info("New patch version")
    version = ".".join(version)
    logging.info(f"New version: v{version}")
    return version


def create_tag(version: str) -> None:
    """
    Create a commit with version update and release new tag on Github.

    :param version: Version that will be released.
    """
    branch_name = subprocess.check_output(["git", "branch", "--show-current"]).decode('ascii')
    logging.info(f"Current branch: {branch_name}")
    if branch_name != MAIN_BRANCH:
        logging.info(f"Switching to branch {MAIN_BRANCH}")
        subprocess.run([f"git checkout '{MAIN_BRANCH}'"], shell=True)
    logging.info(f"Updating branch {MAIN_BRANCH}")
    subprocess.run(["git pull"], shell=True)
    logging.info("Updating setup.py file")
    update_version_setup_file(version)
    logging.info("Committing updates")
    subprocess.run(["git add setup.py"], shell=True)
    subprocess.run([f"git commit -n -m \"New version released v{version}\""], shell=True)
    subprocess.run(["git push"], shell=True)
    logging.info("Committing tag")
    subprocess.run([f"git tag {version}"], shell=True)
    subprocess.run(["git", "push", "origin", f"{version}"])
    if os.path.isdir("dist"):
        shutil.rmtree("dist")
    logging.info(f"Finished process. New version v{version}")


if __name__ == "__main__":
    version = get_new_version()
    # changelog = get_changelog(version)
    # create_tag(version)
    close_milestone(version)
    # create_release(version, changelog)
