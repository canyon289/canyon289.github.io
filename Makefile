.PHONY: publish notebooks devserver preview

publish: notebooks
	bash publish.sh

preview: notebooks
	uv run pelican -s pelicanconf.py
	cd docs && uv run python -m http.server 8000

notebooks:
	uv run python convert_notebooks.py

devserver:
	bash blog.sh
