build:
	pip install .

install-dev:
	$(MAKE) install
	pip install -r requirements.dev.txt

install:
	pip install -r requirements.txt
	$(MAKE) build
