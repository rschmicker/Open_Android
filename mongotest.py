from pymongo import MongoClient
from datetime import datetime

client = MongoClient()
db = client.open_android


total_count = db.apps.find().count()
perm_count = db.apps.find({"permissions":True}).count()
print("Total Permissions:\t" + str(perm_count) + "/" + str(total_count))

string_count = db.apps.find({"strings":True}).count()
print("Total Strings:\t\t" + str(string_count) + "/" + str(total_count))

api_count = db.apps.find({"apis":True}).count()
print("Total API's:\t\t" + str(api_count) + "/" + str(total_count))

smali_count = db.apps.find({"smali":True}).count()
print("Total Smali:\t\t" + str(smali_count) + "/" + str(total_count))

intents_count = db.apps.find({"intents":True}).count()
print("Total Intents:\t\t" + str(intents_count) + "/" + str(total_count))

contain_all_count = db.apps.find({"$and":[{'permissions':True},{'strings':True},{'apis':True},{'smali':True},{'intents':True}]}).count()
print("Containing All:\t\t" + str(contain_all_count) + "/" + str(total_count))