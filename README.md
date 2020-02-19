# lol_beautify_gdocs

# Notice

This library is very much a work in progress. Any help is welcome!

# Installation

- `pip install lol_beautify_gdocs`
- Go to https://developers.google.com/docs/api/quickstart/python
- Generate a `credentials.json` file by pressing "Enable the Google Docs API" button
- Move the file to `~/.config/gsuite_api/credentials.json`

# Usage

Inside the tags you can use champion's names, role names, and in the near future item names.

`[[[name]]]` gets replaced by a 50pt portrait of the champion.

`[[name]]` gets replaced by a 35pt portrait of the champion.

`[name]` gets replaced by a 20pt portrait of the champion.

## Known issues

- By default, google docs transforms your ' in ’, and Riot (wrongly) uses the first one. I will need to make sure 
the code matches champion names properly.

- Currently the module doesn't work for text that is inside inserted tables