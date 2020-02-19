# lol_beautify_gdocs

# Notice

This library is very much a work in progress. Any help is welcome!

# Installation

- `pip install lol_beautify_gdocs`
- Go to https://developers.google.com/docs/api/quickstart/python
- Generate a `credentials.json` file by pressing "Enable the Google Docs API" button
- Move the file to `~/.config/gsuite_api/credentials.json`

# Usage

`25<Braum>`

`50<jungle>`

Inside the tags you can use champion's names, role names, and in the near future item names. The number
represents the picture size, in points.

For role names, I use `top, jungle, mid, bot, supp`.

Other tags include `GOOD, BAD, and ARROW` at the moment. Don't hesitate to ping me if you want to add other ones!

## Known issues

- By default, google docs transforms your ' in ’, and Riot (wrongly) uses the first one. I will need to make sure 
the code matches champion names properly.

- Currently the module doesn't work for text that is inside inserted tables