import datetime
import dateutil.parser
import json
import pymongo

import_file = "data/photo-bank2023-12-29_16:52.json"
#import_file = "data/test-data.json"

import_data = []
import_limit = 10
date_lookup_file = "data/date-lookup.json"
date_lookup = {}

client = pymongo.MongoClient()
db = client["photo-bank"]

with open(import_file) as data_file:
    # JSON record on each line
    for line in data_file:
        import_data.append(json.loads(line))

try:
    with open(date_lookup_file) as lookup_file:
        for d in json.load(lookup_file):
            date_lookup[d['_id']] = dateutil.parser.isoparse(d['datetime'])
except FileNotFoundError:
    print("Didn't find %s" % date_lookup_file)
        
print("%s records to import" % len(import_data))

# Test first 3
for r in import_data:
    if import_limit <= 0: break

    id = r['_id']
    exists = db.photos.find_one({ '_id': id})
    if exists:
        print("Already exists: %s" % id)
    elif 'datetime' in r:
        print("Importing new record %s" % id)

        # Convert date format and handle negative dates too
        ms = r['datetime']['$date']
        dt = datetime.datetime(1970, 1, 1) + datetime.timedelta(milliseconds=ms)
        r['datetime'] = dt

        db.photos.insert_one(r)
        import_limit -= 1

    elif id in date_lookup:
        print("Importing new record %s with date found in lookup" % id)
        r['datetime'] = date_lookup[id]
        db.photos.insert_one(r)
        import_limit -= 1
        
    else:
        print("Cannot import %s, missing datetime" % id)

        
