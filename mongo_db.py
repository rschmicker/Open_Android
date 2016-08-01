import json
import simplejson
import variables
from pymongo import MongoClient
from bson.objectid import ObjectId
import sys

class mongo_db:

	def __init__(self, a, i, s, ap, com):
		client = MongoClient("10.101.1.114")
		self.db = client.open_android
		client.open_android.authenticate("admin", "buckman101", mechanism='MONGODB-CR')
		self.appinfo = a
		self.intents = i
		self.strings = s
		self.apis = ap
		self.com = com
		self.output =variables.mongo_json + self.appinfo.APK_name + "_" + self.appinfo.MD5 + '.json'
		self.dump_data()

	def dump_data(self):

		app_id = ObjectId()
		app_dump = self.db.apps.insert_one(
			{
				"_id": app_id,
				"app_name": self.appinfo.APK_name,
				"version": self.appinfo.APK_version,
				"SHA256": self.appinfo.SHA256,
				"MD5": self.appinfo.MD5,
				"permissions": self.appinfo.perm_exist,
				"intents": self.intents.intent_exist,
				"smali": self.com.smali_exist,
				"strings": self.strings.strings_exist,
				"apis": self.apis.api_exist,
			}
		)
		data = {}
		data['app_name'] = self.appinfo.APK_name
		data['version'] = self.appinfo.APK_version
		data['SHA256'] = self.appinfo.SHA256
		data['MD5'] = self.appinfo.MD5
		data['permissions'] = self.appinfo.perm_exist
		data['intents'] = self.intents.intent_exist
		data['smali'] = self.com.smali_exist
		data['strings'] = self.strings.strings_exist
		data['apis'] = self.apis.api_exist
		with open(self.output, 'w') as outfile:
			json.dump(data, outfile, indent=4, sort_keys=True, separators=(',', ':'))