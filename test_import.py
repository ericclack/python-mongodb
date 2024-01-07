import json
import pymongo

import_file = "data/photo-bank2023-12-29_16:52.json"
import_data = []

client = pymongo.MongoClient()
db = client["photo-bank"]

with open(import_file) as data_file:
    # Not quite JSON format, so read each line in turn
    for line in data_file:
        import_data.append(json.loads(line))

print("%s records to import" % len(import_data))

# Test first 3
for r in import_data[:3]:
    exists = db.photos.find_one({ '_id': r['_id']})
    if exists:
        print("Found %s in database already" % exists)
    else:
        print("New record %s to import" % r['_id'])
