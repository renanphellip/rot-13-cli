.PHONY: install prod format lint test sec config

install:
	@poetry install --no-interaction
	@poetry shell
prod:
	@poetry install --no-interaction --without dev
	@poetry shell
format:
	@isort .
	@blue .
lint:
	@isort . --check
	@blue . --check
	@prospector --no-autodetect rot_cli --with-tool pydocstyle --doc-warning
test:
	@pytest -v rot_cli tests --cov --cov-fail-under 90 --cov-report html
sec:
	@safety check
config:
	@poetry config virtualenvs.in-project true --local
	@make prod
