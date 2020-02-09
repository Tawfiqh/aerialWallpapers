#!/bin/bash
./download_resources.sh
python3 parse_asset_lists.py

# Might need to use your own markdown script/setup here.
cmark --unsafe list_of_files_and_titles.md > html_main.html

cat html_header.html html_main.html html_footer.html > index.html
