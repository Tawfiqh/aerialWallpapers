#!/usr/bin/env python
# coding: utf-8

# In[22]:


import json

# Read the JSON files into an array so we can iterate over them

tvOsReleaseJSON = []

min_os = 10
max_os = 13

for os_number in range(max_os, min_os-1,-1):
    print('tvos',os_number)
    
    with open('./resources/tvos'+str(os_number)+'.json') as json_file:
        dataDict = json.load(json_file)
        tvOsReleaseJSON.append(dataDict);
    
# pandas.read_json('./resources')


# In[24]:


# Setup some functions to parse the JSON that we read in previously.


# `url-1080-H264` (1080p H.264, most compatible format), 
# `url-1080-SDR`  (1080p HEVC, better quality, requires a recent Mac for hardware decoding)
# `url-4K-SDR`    (4K HEVC)

# HDR versions of the above will only play in Catalina (recent/fast Mac recommended)


# ['url', 'accessibilityLabel', 'type', 'id', 'timeOfDay', 'url-1080-SDR', 'url-1080-HDR', 'url-4K-SDR', 'url-4K-HDR', 'pointsOfInterest', 'url-1080-H264']
available_keys = []
# Gets the list of keys from each asset objects.
# Helpful for finding the list of available keys - i.e features available 
def parse_keys_for_asset_list(assets):
    for asset in assets:
        for key in asset.keys():
            if (not key in available_keys):
                available_keys.append(key)





# Each asset object in the assets list has some of the following attributes (at least):
# ["id", "url-1080-SDR", "url-1080-HDR", "url-4K-SDR", "url-4K-HDR", "accessibilityLabel"] 
# accessibilityLabel is the readable one - i.e a decent title.
def _parse_asset_list(assets):
#     print(type(assets)) 
    # Assets is always an array of objects, (found when first run)

    parse_keys_for_asset_list(assets)
    uniform_mode = False; #set this to True to only output url, accesibilityLabel and URLs.
    
    for asset in assets:
        if not uniform_mode:
            parsed_assets[asset['id']]= asset
            
        else:
            new_asset = {}

            new_asset['id'] = asset['id']
            new_asset['accessibilityLabel'] = asset['accessibilityLabel']

            if "url" in asset:
                new_asset['url'] = asset['url']

            if "url-1080-SDR" in asset:
                new_asset['url-1080-SDR'] = asset['url-1080-SDR']

            if "url-1080-HDR" in asset:
                    new_asset["url-1080-HDR"] = asset["url-1080-HDR"]

            if "url-4K-SDR" in asset:
                    new_asset["url-4K-SDR"] = asset["url-4K-SDR"]

            if "url-4K-HDR" in asset:
                    new_asset["url-4K-HDR"] = asset["url-4K-HDR"]

            if "url-1080-H264" in asset:
                    new_asset["url-1080-H264"] = asset["url-1080-H264"]
            parsed_assets[asset['id']]= new_asset # Using an object ensures no duplicates
                


    
def iterate_parse_list_or_array(iterable):
    
    if isinstance(iterable,list):
        for value in iterable:
            iterate_parse_list_or_array(value)

    
    # Iterate over keys if it's a dict
    if isinstance(iterable, dict):
        for key, value in iterable.items():
            if(key == "assets"):
                _parse_asset_list(value)
            else:
                iterate_parse_list_or_array(value)
       

    


# In[25]:


# Iterate over the list of JSON files and parse each one. Each one should somewhere in it have a list of assets. 
# We just search through the keys until we find that list of assets and then we can parse it.

parsed_assets = {}
for tvos in tvOsReleaseJSON:
    iterate_parse_list_or_array(tvos)
    
    
# print(available_keys)
parsed_assets = list(parsed_assets.values())
# print(json.dumps(parsed_assets, indent=4))

with open('output_parsed_file_list.json', 'w', encoding='utf-8') as f:
    json.dump(parsed_assets, f, ensure_ascii=False, indent=4)
    print("succesfully output_parsed_file_list.json")


# In[26]:


import subprocess

# Requires FFMPEG
# https://stackoverflow.com/questions/27568254/how-to-extract-1-screenshot-for-a-video-with-ffmpeg-at-a-given-time
def get_thumbnail(vid_id, url):
    print(url);
    subprocess.call(['ffmpeg', "-ss" ,"00:00:00" ,'-i', url, "-vframes", "1", '-q:v', '1', "thumbnails/"+vid_id+".jpeg"])

    
# Enable this to grab and output thumbnails (to the thumbnails directory) but takes a while
generate_thumbnails = False;

if generate_thumbnails:
    for asset in parsed_assets:
        url = ""
        if "url" in asset:
            url = asset['url']
            
        elif "url-1080-SDR" in asset:
            url = asset["url-1080-SDR"]

        elif "url-1080-H264" in asset:
            url = asset["url-1080-H264"]

        elif "url-1080-HDR" in asset:
            url = asset["url-1080-HDR"]

        elif "url-4K-SDR" in asset:
            url = asset["url-4K-SDR"]

        elif "url-4K-HDR" in asset:
            url = asset["url-4K-HDR"]
        
        if(len(url) > 0):
            get_thumbnail(asset['id'], url)


# In[29]:


markdown_output = []

markdown_output.append("# Aerial wallpapers   ")
markdown_output.append("Amazing footage from Apple, mostly drone footage of various cities. Also satellite footage and underwater footage too! Built off of https://github.com/JohnCoates/Aerial  ")

markdown_output.append('<div class="asset_container" markdown="1">  ')
markdown_output.append("  ")

for asset in parsed_assets:
    markdown_output.append('<div class="asset" markdown="1">  ')
    markdown_output.append("  ")
    
    new_line = "## " + asset['accessibilityLabel'] + " _("+ asset['id'] +")_"
    markdown_output.append(new_line)
    
    # ![Alt text](/path/to/img.jpg "Optional title")
    # images in markdown.
    new_line = "![{}]({} '{}')   ".format(asset['accessibilityLabel'], "thumbnails/"+asset['id']+".jpeg", asset['accessibilityLabel'])
    markdown_output.append(new_line)
    
    markdown_output.append('<div class="button_container" markdown="1">  ')
    markdown_output.append("  ")

    if "url" in asset:
        new_line = "[🎬 Watch ](" + asset['url'] +")   "
        markdown_output.append(new_line)

    if "url-1080-SDR" in asset:
        new_line = "[🎬 Watch 1080p](" + asset['url-1080-SDR'] +")   "
        markdown_output.append(new_line)


    if "url-4K-SDR" in asset:
        new_line = "[🎬 Watch *4K* ](" + asset['url-4K-SDR'] +")   "
        markdown_output.append(new_line)

    if "url-1080-H264" in asset:
        new_line = "[🎬 Watch 1080p-H264 ](" + asset['url-1080-H264'] +")   "
        markdown_output.append(new_line)


    if "url-1080-HDR" in asset or "url-4K-HDR" in asset:
        markdown_output.append(" ")
        markdown_output.append("#### HDR")
        if "url-1080-HDR" in asset:
            new_line = "[🎬 Watch 1080-HDR ](" + asset['url-1080-HDR'] +")   "
            markdown_output.append(new_line)


        if "url-4K-HDR" in asset:
            new_line = "[🎬 Watch 4K-HDR ](" + asset['url-4K-HDR'] +")   "
            markdown_output.append(new_line)
    markdown_output.append("</div>  ")

    markdown_output.append("  ")
    markdown_output.append("</div>  ")
    markdown_output.append("   ");    markdown_output.append("   ")

markdown_output.append("  ")
markdown_output.append("</div>   ")
    
output_markdown_file = "list_of_files_and_titles.md"
with open(output_markdown_file, 'w') as f:
    f.writelines("%s\n" % l for l in markdown_output)
    print("Finished writing to md file:",output_markdown_file)


# In[ ]:




