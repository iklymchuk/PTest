install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv

format:
	black .

lint: 
	pylint --disable=R,C $$(git ls-files '*.py')

all: install lint test format