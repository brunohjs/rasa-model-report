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
DEVELOP_BRANCH = "develop"


def check_params() -> None:
    """
    Check if parameters are valid.
    """
    if len(sys.argv) > 1:
        if sys.argv[1] not in ["major", "minor", "patch"]:
            raise error_message("Invalid version type. Use 'major', 'minor' or 'patch'.")
    if len(sys.argv) > 2:
        if sys.argv[2] not in ["beta"]:
            raise error_message("Invalid version type. Use 'beta'.")


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
        ], shell=True)
        logging.info("")
    else:
        raise error_message(f"Milestone {version} not found.")


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
        raise error_message(f"No notes found for version {version}. Update CHANGELOG.md file.")


def create_release(version: str, notes: str) -> None:
    """
    Create release on Github.

    :param version: Tag version.
    :param notes: Release notes.
    """
    try:
        subprocess.run([
            f"gh release create {version} -R github.com/brunohjs/rasa-model-report --verify-tag --notes \"{notes}\""
        ], shell=True)
        logging.info("Release created on Github.")
    except Exception as error:
        logging.error(f"Could not create release. Error: {error}")


def update_version_setup_file(new_version: str) -> None:
    """
    Update version in setup.py file.

    :param new_version: New version.
    """
    file_path = "rasa_model_report/helpers/constants.py"
    file = open(file_path)
    data = file.read()
    data = re.sub(r"VERSION = \"\d+\.\d+\.\d+(b\d+)?\"", f"VERSION = \"{new_version}\"", data)
    file.close()
    file = open(file_path, "w")
    file.write(data)
    file.close()
    logging.info("Committing updates")
    subprocess.run([f"git add {file_path}"], shell=True)
    subprocess.run([f"git commit -n -m \"New beta version v{version}\""], shell=True)
    subprocess.run(["git push"], shell=True)


def error_message(message: str) -> None:
    """
    Print error message and raise Exception.
    """
    logging.error(message)
    return Exception(message)


def get_latest_version() -> str:
    """
    Get latest version from Github tags.

    :return: Latest version.
    """
    subprocess.run(["git", "fetch", "--all"], shell=False)
    versions = subprocess.check_output(["git", "tag"]).decode('ascii').strip().split('\n')
    version = versions[-1] if versions and versions[0] else '0.0.0'
    return version


def get_new_version_type() -> str:
    """
    Get new version type from command line.

    :return: New version type.
    """
    if len(sys.argv) > 2 and sys.argv[1] in ["major", "minor", "patch"]:
        if sys.argv[1] == "major":
            return "major"
        elif sys.argv[1] == "minor":
            return "minor"
        return "patch"
    raise error_message("Invalid version type. Use 'major', 'minor' or 'patch'.")


def check_beta_version() -> bool:
    """
    Check if new version is a beta version.

    :return: True if new version is a beta version.
    """
    if len(sys.argv) > 2:
        return sys.argv[2] == "beta"
    elif sys.argv:
        return False
    else:
        raise error_message("Invalid version type. Use 'beta'.")


def get_new_version() -> str:
    """
    Get current version from Github tags and return new version.

    :return: New version.
    """
    logging.info("Getting last version")
    version = get_latest_version()
    logging.info(f"Last version: v{version}")
    version = version.split('.')
    version_type = get_new_version_type()
    if "b" in version[2]:
        if check_beta_version():
            splitted_patch = version[2].split("b")
            version[2] = splitted_patch[0]
            version.append("b" + str(int(splitted_patch[1]) + 1))
        else:
            splitted_patch = version[2].split("b")
            version[2] = splitted_patch[0]
    else:
        if check_beta_version():
            version.append("b1")
        if version_type == "major":
            version[0] = str(int(version[0]) + 1)
            version[1] = "0"
            version[2] = "0"
        elif version_type == "minor":
            version[1] = str(int(version[1]) + 1)
            version[2] = "0"
        elif version_type == "patch":
            version[2] = str(int(version[2]) + 1)
    logging.info(f"New {version_type} version")
    version = ".".join(version[:3]) + "".join(version[3:])
    logging.info(f"New version: v{version}")
    return version


def create_tag(version: str, beta_version: bool = False) -> None:
    """
    Create a commit with version update and release new tag on Github.

    :param version: Version that will be released.
    """
    branch_name = subprocess.check_output(["git", "branch", "--show-current"]).decode('ascii')
    logging.info(f"Current branch: {branch_name}")
    if beta_version:
        logging.info("Updating setup.py file")
        update_version_setup_file(version)
        logging.info("Committing tag")
        subprocess.run([f"git tag {version}"], shell=True)
        subprocess.run(["git", "push", "origin", f"{version}"])
        if os.path.isdir("dist"):
            shutil.rmtree("dist")
    else:
        if branch_name != MAIN_BRANCH:
            logging.info(f"Switching to branch {MAIN_BRANCH}")
            subprocess.run([f"git checkout '{MAIN_BRANCH}'"], shell=True)
        logging.info(f"Updating branch {MAIN_BRANCH}")
        subprocess.run(["git pull"], shell=True)
        logging.info("Updating setup.py file")
        update_version_setup_file(version)
        logging.info("Committing tag")
        subprocess.run([f"git tag {version}"], shell=True)
        subprocess.run(["git", "push", "origin", f"{version}"])
        if os.path.isdir("dist"):
            shutil.rmtree("dist")
        logging.info(f"Updating branch {DEVELOP_BRANCH}")
        subprocess.run([f"git checkout '{DEVELOP_BRANCH}'"], shell=True)
        subprocess.run([f"git merge {MAIN_BRANCH}"], shell=True)
        subprocess.run(["git push"], shell=True)
    logging.info(f"Finished process. New version v{version}")


if __name__ == "__main__":
    check_params()
    version = get_new_version()
    beta_version = "b" in version
    create_tag(version, beta_version)
    if not beta_version:
        changelog = get_changelog(version)
        close_milestone(version)
        create_release(version, changelog)
