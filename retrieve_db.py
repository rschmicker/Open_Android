from pymongo import MongoClient
from bson.objectid import ObjectId
import sys

from bson.dbref import DBRef

client = MongoClient()
db = client.open_android

app = db.apps.find_one({"app_name" : "Instagram"},{"string_id":1})
print(app["_id"])
for string in db.strings.find({"_id":app["_id"]}):
	print(string)