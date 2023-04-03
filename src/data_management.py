import json


def import_to_jsonFile(link, shortener):
    with open('data.json', 'r') as f:
        # opened
        data = json.load(f)
        # insert
        data[link] = shortener
        # save
        with open('data.json', 'w') as f:
            json.dump(data, f)


def seach_in_jsonFile(shortenerlink):
    pass
