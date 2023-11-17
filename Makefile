dev: # run the app locally
	poetry run uvicorn nurfa.main:app --reload --log-level debug