import json


with open('./data.json', 'r') as f:
    d = json.load(f)

print(d)

