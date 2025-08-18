activate:
	@& "$(poetry env info --path)\Scripts\Activate.ps1"

run:
	@uvicorn dio_santander_store_api.main:app --reload

precommit-install:
	@poetry run pre-commit install

test:
	@poetry run pytest

test-matching:
	@poetry run pytest -s -rx -k $(K) --pdb dio_santander_store_api ./tests/
