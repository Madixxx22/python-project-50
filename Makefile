gendiff-help:
	poetry run gendiff -h

gendiff:
	poetry run gendiff $(first_file) $(second_file)

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

make coverage:
	poetry run pytest --cov=gendiff --cov-report xml

make check: lint test coverage

build:
	poetry build

install:
	poetry install

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user ./dist/*.whl

.PHONY: gendiff