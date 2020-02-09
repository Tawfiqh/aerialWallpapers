# Aerial wallpapers   

Amazing footage from Apple, mostly drone footage of various cities. Also satellite footage and underwater footage!

Built off of https://github.com/JohnCoates/Aerial  

# Usage
The final result is available here: https://aerial-screensavers.netlify.com

Can  build it yourself with
```sh
./run.sh; open index.html
```

Requires:
- python3
- cmark


`run.sh` first calls `download_resources.sh` that uses curl to fetch the JSON lists of URLs.

`parse_asset_lists.py` then parses this list.  

It has a setting inside to also download thumbnails.

It then outputs a markdown/html file of all of the files, titles, URLs, link to thumbnails.

Markdown is used as it's a little bit easier than crafting all of the HTML. But some divs are used in the markdown so that it's more easily styled with CSS and flexbox, padding, borders etc.

The markdown file is compiled into HTML. It then has an HTML header/footer appended to it. This footer references the CSS.

The final web-page is output as `index.html`.
