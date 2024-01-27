import datetime
import dateutil.parser
import json
import pymongo
from pprint import pprint

client = pymongo.MongoClient()
db = client["photo-bank"]

for photo in db.photos.find():
    # Fix dates
    photo['datetime'] = photo['datetime'].isoformat()

    print(json.dumps(photo))
