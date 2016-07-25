from pymongo import MongoClient
from bson.objectid import ObjectId

class mongo_api:

	def __init__(self, host, port, dbname, collection):
		self.host = host
		self.port = port
		self.dbname = dbname
		client = MongoClient(self.host, self.port)
		self.db = client[self.dbname]
		self.collection = self.db[collection]

	def list_feature(self, feature_list, by):
		doc_list = []
		query = {}
		for feature in feature_list:
			query[feature] = True
		result = self.collection.find(query)
		for doc in result:
			form_list = []
			for form in by:
				form_list.append(doc[form])
			doc_list.append(form_list)
		return doc_list

	def list_apk_names(self):
		apk_list = []
		result = self.collection.find()
		for doc in result:
			print(doc["app_name"])
			apk_list.append(doc["app_name"])
		return apk_list

	def feature_exist(self, app, feature):
		result = self.collection.find({"app_name":app})
		for doc in result:
			exist = doc[feature]
		return exist

	def list_all_mongo(self):
		all_data = []
		result = self.collection.find()
		for data in result:
			values = data.values()
			app_name = data.get("app_name")
			values.remove(data.get("app_name"))
			values.insert(0,app_name)
			all_data.append(values)
		return all_data

	def get_all_fields(self):
		fields = []
		result = self.collection.find_one()
		for data in result:
			fields.append(data)
		fields = fields[:-1]
		fields.remove("app_name")
		fields.insert(0,"app_name")
		return(fields)