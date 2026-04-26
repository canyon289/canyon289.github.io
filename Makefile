.PHONY: publish notebooks devserver

publish: notebooks
	bash publish.sh

notebooks:
	uv run python convert_notebooks.py

devserver:
	bash blog.sh
