build-package:
	pip install . --force-reinstall
	python -m build

public-test: build-package
	twine upload -r testpypi dist/* -u brunohjs -p "K6vqVPX2Yl0g;H86br5f"

public-prod: build-package
	twine upload -r pypi dist/* -u brunohjs -p "K6vqVPX2Yl0g;H86br5f"

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
