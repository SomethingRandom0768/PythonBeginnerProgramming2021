import json

filename = 'favorite_number.json'

with open(filename) as f:
    fav_number = json.load(f)

print(f"I know your favorite number, it's {fav_number}")