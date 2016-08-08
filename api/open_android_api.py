from mongo_api import *
from solr_api import *
from lxml import etree
import variables
import csv
import json
import sys
import os


class open_android_api:

	def __init__(self):

		self.mongo_csv_location = variables.mongo_csv_location
		self.mongo_json_location = variables.mongo_json_location
		self.mongo_xml_location = variables.mongo_xml_location

		self.solr_csv_location = variables.solr_csv_location
		self.solr_json_location = variables.solr_json_location
		self.solr_xml_location = variables.solr_xml_location

		self.m = mongo_api("localhost", 27017, "reader", "reader" "open_android", "apps")
		self.s = solr_api("localhost", 8983)

	def get_features_from_solr(self, search_for, features, return_type):
		to_output = self.s.list_feature(search_for, features, return_type)
		if return_type == "csv":
			self.csv_builder(features, to_output, "solr")
		elif return_type == "json":
			self.json_builder(features, to_output, "solr")
		elif return_type == "xml":
			self.xml_builder(features, to_output, "solr")

	def get_features_from_mongo(self, by, features, return_type):
		to_output = self.m.list_feature(by, features)
		if return_type == "csv":
			self.csv_builder(features, to_output, "mongo")
		elif return_type == "json":
			self.json_builder(features, to_output, "mongo")
		elif return_type == "xml":
			self.xml_builder(features, to_output, "mongo")

	def xml_builder(self, features, data, data_location):
		reload(sys)  
		sys.setdefaultencoding('utf-8')
		if (data_location == "mongo"):
			if (os.path.isfile(self.mongo_xml_location)):
				os.remove(self.mongo_xml_location)
		else:
			if (os.path.isfile(self.solr_xml_location)):
				os.remove(self.solr_xml_location)
		for element in data:
			values = []
			for value in element:
				values.append(value)
			root = etree.Element(features[0])
			if values[0] == "":
				root.text = "NOT_FOUND"
			else:
				root.text = values[0].decode('utf-8')
			for i in range(1,len(features)):
				child = etree.Element(features[i])
				if values[i] == True:
					child.text = "1"
				elif values[i] == False:
					child.text = "0"
				else:
					child.text = str(values[i])
				root.append(child)
			s = etree.tostring(root, pretty_print=True)
			if (data_location == "mongo"):
				f = open(self.mongo_xml_location,'a')
			else:
				f = open(self.solr_xml_location,'a')
			f.write(s)

	def json_builder(self, features, data, data_location):
		json_data = {}
		if (data_location == "mongo"):
			if (os.path.isfile(self.mongo_json_location)):
				os.remove(self.mongo_json_location)
		else:
			if (os.path.isfile(self.solr_json_location)):
				os.remove(self.solr_json_location)
		for element in data:
			values = []
			for value in element:
				values.append(value)
			json_data[features[0]] = values[0]
			for i in range(1,len(features)):
				json_data[features[i]] = str(values[i])
			if (data_location == "mongo"):
				with open(self.mongo_json_location, 'a') as outfile:
					json.dump(json_data, outfile, indent=4, sort_keys=True, separators=(',', ':'))
			else:
				with open(self.solr_json_location, 'a') as outfile:
					json.dump(json_data, outfile, indent=4, sort_keys=True, separators=(',', ':'))
		
	
	def csv_builder(self, features, data, data_location):
		reload(sys)  
		sys.setdefaultencoding('utf-8')
		if (data_location == "mongo"):
			csv_file = open(self.mongo_csv_location, 'wt')
		else:
			csv_file = open(self.solr_csv_location, 'wt')
		fields = features
		writer = csv.DictWriter(csv_file, fieldnames=fields)
		headers = {}
		headers = dict( (n,n) for n in fields )
		writer.writerow(headers)

		for i in range(len(data)):
			dict_builder = {}
			for k in range(len(fields)):
				dict_builder[fields[k]] = data[i][k]
			writer.writerow(dict_builder)

# open connection to mongo and solr	
o = open_android_api()

# Create file with mongo features ([list of features to check for existence], [features to write to file], return type)
# For xml, the first feature to output will be the root, the rest will all be children
o.get_features_from_mongo(["permissions", "strings"], ["app_name", "version", "MD5"], "csv")
#o.get_features_from_mongo(["permissions", "strings"], ["app_name", "version", "MD5", "permissions", "apis", "strings"], "xml")
#o.get_features_from_mongo(["permissions", "strings"], ["app_name", "version", "MD5", "permissions", "apis", "strings"], "json")
#o.csv_builder(o.m.get_all_fields(),o.m.list_all_mongo(),"mongo")
#o.json_builder(o.m.get_all_fields(),o.m.list_all_mongo(),"mongo")
#o.xml_builder(o.m.get_all_fields(),o.m.list_all_mongo(),"mongo")
# Create file with solr features ("regex string", [list of features to extract], return type)
#o.get_features_from_solr("*:*", ["app_version", "permissions", "permissions_vector"], "xml")
#o.get_features_from_solr("*:*", ["app_version", "permissions", "permissions_vector", 
#o.get_features_from_solr("*:*", ["app_version", "permissions", "permissions_vector", 
