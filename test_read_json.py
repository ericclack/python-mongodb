import json

file = "data/photo-bank2023-12-29_16:52.json"

data = []

with open(file) as data_file:
    # Not quite JSON format, so read each line in turn
    for line in data_file:
        data.append(json.loads(line))

print(len(data))
