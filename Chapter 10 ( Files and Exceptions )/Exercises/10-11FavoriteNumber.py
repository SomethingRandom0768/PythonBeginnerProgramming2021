import json

favorite_num = input("What's your favorite number? ")

filename = 'favorite_number.json'

with open(filename, 'w') as f:
    json.dump(favorite_num, f)