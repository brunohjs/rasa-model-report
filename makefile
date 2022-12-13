build-package:
	pip install . --force-reinstall
	python -m build

public-test: build-package
	twine upload -r testpypi dist/* -u brunohjs -p "K6vqVPX2Yl0g;H86br5f"

public-prod: build-package
	twine upload -r pypi dist/* -u brunohjs -p "K6vqVPX2Yl0g;H86br5f"

install-dev:
	pip install . -r requirements.dev.txt

install:
	pip install .

test:
	pytest
	python scripts/change_coverage_badge.py

release-patch:
	python scripts/release.py patch && $(MAKE) public-prod

release-minor:
	python scripts/release.py minor && $(MAKE) public-prod

release-major:
	python scripts/release.py major && $(MAKE) public-prod

update-coverage:
	python scripts/change_coverage_badge.py
