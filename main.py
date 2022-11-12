import json
import selenium

# get data from config file
with open('config.json', 'r') as f:
    data = json.load(f)

# const variables
SEARCH_ITEM = data["inputs"]["SEARCH_ITEM"]
