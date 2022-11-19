import glob
import os.path
import shutil


def create_dir(dir_name):
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)


def remove_dir(dir_name):
    if os.path.isdir(dir_name):
        shutil.rmtree(dir_name)


def remove_generated_files(rasa_path):
    files_to_find = (f"{rasa_path}/**/overview.json", f"{rasa_path}/**/report.md", "**/test.csv")
    files = []
    for file in files_to_find:
        files.extend(glob.glob(file, recursive=True))
    for file in files:
        if os.path.isfile(file):
            os.remove(file)
