build:
	pip install . --force-reinstall

install-dev:
	pip install . -r requirements.txt -r requirements.dev.txt

install:
	pip install . -r requirements.txt

test:
	pytest
	python scripts/change_coverage_badge.py

release-patch:
	python scripts/release.py patch

release-minor:
	python scripts/release.py minor

release-major:
	python scripts/release.py major

update-coverage:
	python scripts/change_coverage_badge.py
