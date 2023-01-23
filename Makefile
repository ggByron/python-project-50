gendiff:
	poetry run gendiff
	
install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=hexlet_python_package --cov-report xml

lint:
	poetry run flake8 hexlet_python_package

selfcheck:
	poetry check

check: selfcheck test lint

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	pip install --user --force-reinstall dist/*.whl

.PHONY: install test lint selfcheck check build