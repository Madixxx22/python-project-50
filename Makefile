gendiff-help:
	poetry run gendiff -h

gendiff:
	poetry run gendiff filepath1.json filepath2.json

build:
	poetry build