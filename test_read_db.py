import pymongo
client = pymongo.MongoClient()

db = client["photo-bank"]

for r in db.photos.find():
    print(r['name'])
