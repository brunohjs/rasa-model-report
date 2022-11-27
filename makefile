build:
	pip install . --force-reinstall

install-dev:
	$(MAKE) install
	pip install -r requirements.dev.txt

install:
	pip install -r requirements.txt
	$(MAKE) build

test:
	pytest

release-patch:
	python3 release.py patch

release-minor:
	python3 release.py minor

release-major:
	python3 release.py major
