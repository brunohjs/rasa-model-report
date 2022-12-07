import re
from xml.dom import minidom


def get_color(value):
    if value >= 0.95:
        return "brightgreen"
    elif value >= 0.8:
        return "green"
    elif value >= 0.6:
        return "yellow"
    elif value >= 0.3:
        return "orange"
    elif value >= 0.1:
        return "red"
    else:
        return "lightgrey"


def get_coverage():
    file = minidom.parse("coverage.xml")
    coverage = file.getElementsByTagName("coverage")
    if coverage:
        total = coverage[0].attributes["lines-valid"].value
        coveraged = coverage[0].attributes["lines-covered"].value
        return int(coveraged) / int(total)
    return 0


def change_coverage(new_value, new_color):
    new_value = int(new_value * 100)
    file = open("README.md", "r")
    data = file.read()
    file.close()
    data = re.sub(
        r"label=coverage&message=[0-9.]+%&color=[a-z]+",
        f"label=coverage&message={new_value}%&color={new_color}",
        data
    )
    file = open("README.md", "w")
    file.write(data)


if __name__ == "__main__":
    new_coverage = get_coverage()
    change_coverage(new_coverage, get_color(new_coverage))
