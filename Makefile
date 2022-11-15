.PHONY: install format lint test sec

install:
	@poetry install
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
	@make install
