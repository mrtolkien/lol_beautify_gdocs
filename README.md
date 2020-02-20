# lol_beautify_gdocs

# Notice

This library is very much a work in progress. Any help is welcome!

# Installation

- `pip install lol_beautify_gdocs`
- Go to https://developers.google.com/docs/api/quickstart/python
- Generate a `credentials.json` file by pressing "Enable the Google Docs API" button
- Move the file to `~/.config/gsuite_api/credentials.json`

# Usage

Add tags formatted as `size<object>` in your google document. Afterwards, call `lol_beautify_gdocs.beautify_document(URL)` with your document's URL.

Example tags: `25<Braum>`, `50<jungle>`

Inside the tags you can use champion's names, role names, item names, and some custom tags. The number
represents the picture size, in points.

For role names, I use `top, jungle, mid, bot, supp`.

Other tags include `GOOD, BAD, and ARROW` at the moment. Don't hesitate to ping me if you want to add other ones!

## Known issues

- Currently the module doesn't work for text that is inside tables.
