# MediaWiki(mw) to Markdown(md) Converter for QB64PE Wiki
> Author:  Rick Christy
> Email:   grymmjack@gmail.com
> Website: https://grymmjack.github.io

This script fetches HTML content from the QB64PE wiki 
using a list of keywords (keywords.txt) and converts
the content to Markdown format. The Markdown content is
then saved to individual .md files in a specified directory.

> The purpose of this script is to populate `/qb64pe/internal/help/*.md`
> markdown help files for hover help in the [QB64PE VSCode Extension](https://github.com/grymmjack/qb64pe-vscode)

## INSTALL
* Clone this repo: `gh repo clone grymmjack/qb64pe-wiki-to-markdown`
* Setup venv: `python -mvenv .venv`
* Activate venv: `source .venv/bin/activate`
* Install packages: `pip install -r requirements.txt`

## USAGE
* With virtual environment active (`source .venv/bin/activate`)
* Run: `python mw-to-md.py`

That's it!