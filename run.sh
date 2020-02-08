#!/bin/bash
./download_resources.sh
python3 parse_asset_lists.py

# Might need to use your own markdown script/setup here.
perl ./Markdown.pl list_of_files_and_titles.md > index.html 
