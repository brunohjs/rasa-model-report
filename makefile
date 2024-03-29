ifneq ("$(wildcard .env)","")
	include .env
endif

# Build.
build-package:
	pip install . --force-reinstall
	python -m build

# Public new version on PyPI test environment.
public-test: build-package
	twine upload -r testpypi dist/* -u "${PYPI_TEST_USERNAME}" -p "${PYPI_TEST_PASSWORD}"

# Public new version on PyPI production environment.
public-prod: build-package
	twine upload -r pypi dist/* -u "${PYPI_PROD_USERNAME}" -p "${PYPI_PROD_PASSWORD}"

# Install development dependencies.
install-dev:
	pip install . -r requirements.dev.txt

# Install building dependencies.
install:
	pip install .

# Execute unit tests and update README.md coverage badge.
test:
	pytest
	python scripts/change_coverage_badge.py

# Create new test patch version and public on PyPI.
release-patch-beta:
	python scripts/release.py patch beta && $(MAKE) public-prod

# Create new test minor version and public on PyPI.
release-minor-beta:
	python scripts/release.py minor beta && $(MAKE) public-prod

# Create new test major version and public on PyPI.
release-major-beta:
	python scripts/release.py major beta && $(MAKE) public-prod

# Create new production patch version and public on PyPI.
release-patch:
	python scripts/release.py patch && $(MAKE) public-prod

# Create new production minor version and public on PyPI.
release-minor:
	python scripts/release.py minor && $(MAKE) public-prod

# Create new production major version and public on PyPI.
release-major:
	python scripts/release.py major && $(MAKE) public-prod

# Update README.md coverage badge.
update-coverage:
	python scripts/change_coverage_badge.py

# Generate Rasa model report.
report:
	pip install . && rasa-model-report --path tests/mocks/rasa.v3/ --actions-path tests/mocks/rasa.v3/actions/ --rasa-version 3.5.2 --disable-nlu --no-images --exclude utter_uncovered
