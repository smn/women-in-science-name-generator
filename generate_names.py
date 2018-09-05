import re
import json
import random
import unicodedata
import csv
import sys

with open('scientists.json', 'r') as fp:
    scientists = json.load(fp)

writer = csv.writer(sys.stdout)

for scientist in scientists:
    name = scientist["name"]

    # pulled from Django's slugify template filter
    allow_unicode = False

    if allow_unicode:
        name = unicodedata.normalize('NFKC', name)
    else:
        name = unicodedata.normalize('NFKD', name).encode('ascii', 'ignore').decode('ascii')

    name = re.sub(r'[^\w\s-]', '', name).strip().lower()
    slug = re.sub(r'[-\s]+', '-', name)
    writer.writerow([slug, scientist["name"], scientist["description"]])
