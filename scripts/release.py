# This script is responsable for launching new app releases.
import logging
import re
import subprocess
import sys


logging.basicConfig(format="%(asctime)s [%(levelname)s] %(message)s", level=logging.INFO)
MAIN_BRANCH = "#10"


def update_version_setup_file(new_version):
    file = open("setup.py")
    data = file.read()
    data = re.sub(r"version=\"\d+\.\d+\.\d+\",", f"version=\"{new_version}\",", data)
    file.close()
    file = open("setup.py", "w")
    file.write(data)
    file.close()


def get_version():
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


def release(version):
    branch_name = subprocess.check_output(["git", "branch", "--show-current"]).decode('ascii')
    logging.info(f"Current branch: {branch_name}")
    if branch_name != MAIN_BRANCH:
        logging.info(f"Switching to branch {MAIN_BRANCH}")
        subprocess.run(["git checkout", f"'{MAIN_BRANCH}'"], shell=True)
    logging.info(f"Updating branch {MAIN_BRANCH}")
    subprocess.run(["git pull"], shell=True)
    logging.info("Updating setup.py file")
    update_version_setup_file(version)
    logging.info("Committing updates")
    subprocess.run(["git add", "setup.py"], shell=True)
    subprocess.run(["git commit", "-n", "-m", f"New version released v{version}"], shell=True)
    subprocess.run(["git push"], shell=True)
    logging.info("Committing tag")
    subprocess.run(["git tag", f"{version}"], shell=True)
    subprocess.run(["git push", "--tags"])
    logging.info(f"Finished process. New version v{version}")


if __name__ == "__main__":
    version = get_version()
    release(version)
