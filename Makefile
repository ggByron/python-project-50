install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

check: selfcheck test lint

.PHONY: install test lint selfcheck check build

build:
	poetry build

package-install:
	pip install --user --force-reinstall dist/*.whl

package-reinstall:
	pip install --user --force-reinstall dist/*.whl

publish:
	poetry publish --dry-run

gendiff:
	poetry run gendiff -h