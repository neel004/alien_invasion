PYTHON=python3.10

bin/python:
	$(PYTHON) -m venv .
	bin/pip install --upgrade pip

install: bin/python
	bin/pip install -r requirements.txt

dev: install
	bin/pip install -r test-requirements.txt
