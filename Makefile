.PHONY: publish notebooks devserver preview

publish: notebooks
	bash publish.sh

preview: notebooks
	uv run pelican -lr -s pelicanconf.py

notebooks:
	uv run python convert_notebooks.py

devserver:
	bash blog.sh
