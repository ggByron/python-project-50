gendiff:
		poetry run gendiff -h
	
install:
		poetry install

pytest:
		poetry run pytest

test-coverage:
		poetry run pytest --cov=gendiff --cov-report xml

lint:
		poetry run flake8 gendiff

check: selfcheck pytest lint

build:
		poetry build

publish:
		poetry publish --dry-run

package-install:
		pip install --user --force-reinstall dist/*.whl
