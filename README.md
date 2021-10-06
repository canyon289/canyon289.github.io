# Website with Pelican

# Setup

Use python version 3.6.

# Page and Article Organization

Markdown files live in the `content` folder under `pages` or `articles`. Below is a recommendation of how to keep the workspace organized, although there are no constraints that enforce this in Pelican.

## Pages

Any page that will appear on the navigation bar will be in the first level with the `status: published`.

References will go under the `pages/references` folder with the `status: hidden`. They will be manually linked with [References.md](content/pages/References.md).

Any other hidden page will go under `pages/other_hidden`.

## Articles

Articles will be in folders named by their category. This will help enforce the constraint that each article can have up to 1 category.

# Custom Theme Organization

The custom theme is based on the [Hugo Whisper theme](https://hugo-whisper.netlify.app/docs/install-hugo/). 

The `static` folder contains the main CSS and JS files.

The `templates` folder contains the HTML. Different files (articles, pages, categories, etc.) extend `base.html` and have the same filename as their type. The only exception is the blog landing page, which is `index.html`.

# MetaData for Markdown

You can add the following metadata (and more) to your markdown files, but the custom theme only uses a few from the list. You can adjust the usage by editing `/custom/templates/article.html` and `custom/templates/base.html`.

| Metadata | Description | Custom Theme Usage |
| -------- | ----------- | ------------------ |
| title | Title of the article or page | Used |
| date | Publication date (e.g., YYYY-MM-DD HH:SS) | Used - only for articles |
| modified | Modification date (e.g., YYYY-MM-DD HH:SS) | Not used |
| tags | Content tags, separated by commas | Used |
| keywords | Content keywords, separated by commas (HTML content only) | Not used |
| category | Content category (one only — not multiple) | Used |
| slug | Identifier used in URLs and translations | Used |
| author | Content author, when there is only one | Used |
| authors | Content authors, when there are multiple | Not used |
| summary | Brief description of content for index pages | Not used |
| lang | Content language ID (en, fr, etc.) | Not used |
| translation | If content is a translation of another (true or false) | Not used |
| status | Content status: draft, hidden, or published | Used - published pages will show on the navigation bar |
| template | Name of template to use to generate content (without extension) | Not used |
| save_as | Save content to this relative file path | Not used |
| url | URL to use for this article/page | Not used |

# Other Notes

* Do some checks when installing new Plugins. Sometimes the CSS for the new plugin will override/conflict with the main CSS.
