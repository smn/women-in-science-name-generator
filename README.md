# Women in Science

Pulls the [List of female scientists in the 20th century](https://en.wikipedia.org/wiki/List_of_female_scientists_in_the_20th_century) from Wikipedia and
generates a JSON file with their name and a 1 line description of their work.

To fetch the names and write the JSON file:

> python fetch_scientists.py > scientists.json

To read the JSON file and generate a CSV with `url-friendly-name,name,description` rows:

> python generate_names.py scientists.json > scientists-slugs-and-names.csv

Useful for generating names like:

- `alba-zaluar`
- `margaret-mead`
- `lily-chitty`

**This file is probably python 3 only**
