# Aerial wallpapers   

Amazing footage from Apple, mostly drone footage of various cities. Also satellite footage and underwater footage!

Built off of https://github.com/JohnCoates/Aerial  
Similar list available here: https://bzamayo.com/watch-all-the-apple-tv-aerial-video-screensavers

This repo contains 3 main parts:

1. Python notebook to create "output_parsed_file_list.json" and scrape thumbnails.
2. index.html which is a static html page showing all the thumbnails and linking to the videos. Inefficient  as it loads all the thumbnails on-load.
3. gatsby/ folder - a [gatsby](http://gatsbyjs.org) site - the same as index.html but loads images more efficiently.


# Building it
The final result is available here: https://aerial-screensavers.netlify.com a deployed version of the gatsby site.

You can and run build it yourself with
```sh
./run.sh;
open index.html
```

Requires:
- python3
- cmark

`run.sh` first calls `download_resources.sh` that uses curl to fetch the JSON lists of URLs.
_These were pulled from_

`parse_asset_lists.py` then parses this list.

It has a setting inside to also download thumbnails.

It then outputs a markdown/html file of all of the files, titles, URLs, link to thumbnails.

Markdown is used as it's a little bit easier than crafting all of the HTML. But some divs are used in the markdown so that it's more easily styled with CSS and flexbox, padding, borders etc.

The markdown file is compiled into HTML. It then has an HTML header/footer appended to it. This footer references the CSS.

The final web-page is output as `index.html`.
