#!/usr/bin/env python3
"""
Append GenAiGuidebook URLs to the Pelican-generated sitemap.xml.

Reads ~/repos/GenAiGuidebook/genaiguidebook/_toc.yml, converts every
file: entry to its ravinkumar.com/GenAiGuidebook/... URL, and appends
them to ../docs/sitemap.xml (relative to dev/).

Run as part of the publish flow:
    uv run pelican -s publishconf.py && uv run python append_guidebook_sitemap.py
"""
from pathlib import Path
import xml.etree.ElementTree as ET
import yaml  # PyYAML, installed transitively via pelican

TOC_PATH = Path.home() / "repos/GenAiGuidebook/genaiguidebook/_toc.yml"
SITEMAP_PATH = Path("docs/sitemap.xml")
BASE_URL = "https://ravinkumar.com/GenAiGuidebook"
NS = "http://www.sitemaps.org/schemas/sitemap/0.9"


def toc_file_to_url(file_str: str) -> str:
    """Convert a _toc.yml file: value to its published HTML URL."""
    p = Path(file_str)
    # Drop .ipynb / .md suffix and replace with .html
    if p.suffix in (".ipynb", ".md"):
        p = p.with_suffix(".html")
    else:
        p = Path(str(p) + ".html")
    return f"{BASE_URL}/{p.as_posix()}"


def extract_urls_from_toc(toc: dict) -> list[str]:
    """Walk the jb-book TOC and collect all file: entries as URLs."""
    urls = []

    # root page
    if "root" in toc:
        urls.append(toc_file_to_url(toc["root"]))

    for part in toc.get("parts", []):
        for chapter in part.get("chapters", []):
            if "file" in chapter:
                urls.append(toc_file_to_url(chapter["file"]))
            # nested sections (if any)
            for section in chapter.get("sections", []):
                if "file" in section:
                    urls.append(toc_file_to_url(section["file"]))

    return urls


def main():
    if not TOC_PATH.exists():
        raise FileNotFoundError(f"TOC not found: {TOC_PATH}")
    if not SITEMAP_PATH.exists():
        raise FileNotFoundError(
            f"sitemap.xml not found at {SITEMAP_PATH}. "
            "Run 'uv run pelican -s publishconf.py' first."
        )

    toc = yaml.safe_load(TOC_PATH.read_text())
    new_urls = extract_urls_from_toc(toc)

    ET.register_namespace("", NS)
    tree = ET.parse(SITEMAP_PATH)
    root = tree.getroot()

    existing = {
        el.text
        for url in root.findall(f"{{{NS}}}url")
        if (el := url.find(f"{{{NS}}}loc")) is not None
    }

    added = 0
    for url in new_urls:
        if url in existing:
            continue
        url_el = ET.SubElement(root, f"{{{NS}}}url")
        ET.SubElement(url_el, f"{{{NS}}}loc").text = url
        ET.SubElement(url_el, f"{{{NS}}}changefreq").text = "monthly"
        ET.SubElement(url_el, f"{{{NS}}}priority").text = "0.7"
        added += 1

    ET.indent(tree, space="  ")
    tree.write(SITEMAP_PATH, xml_declaration=True, encoding="utf-8")
    print(f"✅ Appended {added} GenAiGuidebook URLs to {SITEMAP_PATH}")
    print(f"   ({len(new_urls) - added} already present)")


if __name__ == "__main__":
    main()
