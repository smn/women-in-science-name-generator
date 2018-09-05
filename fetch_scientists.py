import requests
import re
import json
import sys

response = requests.get(
    "https://en.wikipedia.org/w/api.php",
    params={
        "action": "query",
        "prop": "revisions",
        "rvprop": "content",
        "format": "json",
        "titles": "List_of_female_scientists_in_the_20th_century"
    }).json()

[(page_id,page)] = response["query"]["pages"].items()
media_text = page["revisions"][0]["*"]

pattern = re.compile(r'\*\s?\[\[([\w\-\s]+)\]\],? ([^<\n]+)', re.MULTILINE)

matches = re.findall(pattern, media_text)

scientists = [
    {"name": scientist, "description": description.replace('[', '').replace(']', '')}
    for (scientist, description) in matches]

json.dump(scientists, sys.stdout)
