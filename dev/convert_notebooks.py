#!/usr/bin/env python3
"""
One-time notebook → Markdown conversion script.
Replaces the old pelican-liquid-tags approach.

Run from dev/ after: uv sync
Usage:  uv run python convert_notebooks.py
"""
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

NOTEBOOKS_DIR = Path("content/notebooks")
OUTPUT_STATS_DIR = Path("content/articles/Statistics")
IMAGES_DIR = Path("content/images/notebooks")

NOTEBOOKS = [
    {
        "file": "BayesianGlossary.ipynb",
        "skip_cells": 1,  # skip first cell (notebook title cell)
        "output_slug": "BayesianGlossary",
        "frontmatter": (
            "Title: Bayesian Glossary\n"
            "Date: 2019-01-14\n"
            "Category: Statistics\n"
            "Slug: BayesianGlossary\n"
            "Authors: Ravin Kumar\n"
            "Status: Published\n"
            "Tags: Reference\n"
        ),
        "intro": "",
    },
    {
        "file": "InferenceCheatsheet.ipynb",
        "skip_cells": 1,
        "output_slug": "InferenceCheatsheet",
        "frontmatter": (
            "Title: Bayesian Inference Cheatsheet\n"
            "Date: 2019-02-07\n"
            "Category: Statistics\n"
            "Tags: Reference\n"
            "Slug: InferenceCheatsheet\n"
            "Authors: Ravin Kumar\n"
            "Status: Published\n"
        ),
        "intro": "",
    },
    {
        "file": "Random_Variable_Algebra.ipynb",
        "skip_cells": 0,
        "output_slug": "RandomVariableAlgebra",
        "frontmatter": (
            "Title: Random Variable Algebra Simulation and Intuition\n"
            "Date: 2021-09-22\n"
            "Category: Statistics\n"
            "Tags: Statistics\n"
            "Slug: RandomVariableAlgebra\n"
            "Authors: Ravin Kumar\n"
            "Status: Published\n"
        ),
        "intro": (
            "Random Variable Algebra can be challenging to understand mathematically "
            "and can sometimes feel counterintuitive. Things that have helped me are "
            "learning the wrong ways to perform RV Algebra as well as numerical "
            "simulation, both of which are presented in the notebook below.\n\n"
            "A recording of me talking over slides is available "
            "[on Youtube](https://www.youtube.com/watch?v=6BklWi2b6vY). "
            "You can download the notebook "
            "[from Github](https://github.com/canyon289/canyon289.github.io/tree/master/dev/content/notebooks/Random_Variable_Algebra.ipynb)\n\n"
            "Happy Learning!\n"
        ),
    },
    {
        "file": "bayesian_decision_making.ipynb",
        "skip_cells": 0,
        "output_slug": "BayesianDecisionMaking",
        "frontmatter": (
            "Title: Bayesian Decision Making\n"
            "Date: 2019-01-14\n"
            "Category: Statistics\n"
            "Tags: Bayes, Manufacturing\n"
            "Slug: BayesianDecisionMaking\n"
            "Authors: Ravin Kumar\n"
            "Status: Published\n"
        ),
        "intro": "",
    },
]


def load_notebook_trimmed(path: Path, skip_cells: int) -> dict:
    """Load notebook JSON and remove the first N cells."""
    nb = json.loads(path.read_text())
    if skip_cells:
        nb["cells"] = nb["cells"][skip_cells:]
    return nb


def convert_notebook(nb_dict: dict, slug: str, tmp_dir: Path) -> Path:
    """Write trimmed notebook to tmp, run nbconvert, return the .md path."""
    tmp_nb = tmp_dir / f"{slug}.ipynb"
    tmp_nb.write_text(json.dumps(nb_dict))
    subprocess.run(
        [
            sys.executable, "-m", "nbconvert",
            "--to", "markdown",
            "--output", slug,
            "--output-dir", str(tmp_dir),
            str(tmp_nb),
        ],
        check=True,
    )
    return tmp_dir / f"{slug}.md"


def fix_image_paths(md_text: str, slug: str) -> str:
    """
    nbconvert writes image refs like:  ![png](BayesianGlossary_files/output_4_1.png)
    Rewrite them to Pelican static paths:  ![png]({static}/images/notebooks/BayesianGlossary_files/output_4_1.png)
    """
    return re.sub(
        rf"!\[([^\]]*)\]\({re.escape(slug)}_files/([^)]+)\)",
        rf"![\1]({{static}}/images/notebooks/{slug}_files/\2)",
        md_text,
    )


def main():
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory() as tmp_str:
        tmp_dir = Path(tmp_str)

        for spec in NOTEBOOKS:
            slug = spec["output_slug"]
            nb_path = NOTEBOOKS_DIR / spec["file"]
            print(f"\n→ Converting {spec['file']} ...")

            nb_dict = load_notebook_trimmed(nb_path, spec["skip_cells"])
            md_path = convert_notebook(nb_dict, slug, tmp_dir)

            # Move extracted images (_files/) into content/images/notebooks/
            files_src = tmp_dir / f"{slug}_files"
            if files_src.exists():
                files_dst = IMAGES_DIR / f"{slug}_files"
                if files_dst.exists():
                    shutil.rmtree(files_dst)
                shutil.copytree(files_src, files_dst)
                print(f"  images → {files_dst}")

            # Build final markdown content
            md_body = md_path.read_text()
            md_body = fix_image_paths(md_body, slug)

            final = spec["frontmatter"] + "\n"
            if spec["intro"]:
                final += spec["intro"] + "\n"
            final += md_body

            out_path = OUTPUT_STATS_DIR / f"{slug}.md"
            out_path.write_text(final)
            print(f"  written → {out_path}")

    print("\n✅ All notebooks converted. You can now delete dev/_nb_header.html")


if __name__ == "__main__":
    main()
