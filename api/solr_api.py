import urllib2
import subprocess
import variables
import re

class solr_api:

	def __init__(self, hostname, port):
		self.solr_dir = variables.solr_dir
		self.core = variables.solr_collection_name
		self.hostname = hostname
		self.port = port
		self.base_url = "http://" + self.hostname + ":" + str(self.port) + "/solr/" + self.core + "/"

	def list_feature(self, search, fields, return_type):
		perm_index = -1
		IP_index = -1
		Phone_index = -1
		URL_index = -1
		sys_index = -1
		try:
			sys_index = fields.index("sys_cmd_vector")
			sys_cmd_vector_list = self.get_sys_cmd_vector()
			fields.remove("sys_cmd_vector")
		except ValueError:
			pass

		try:
			perm_index = fields.index("permissions_vector")
			permissions_vector_list = self.get_permissions_vector()
			fields.remove("permissions_vector")
		except ValueError:
			pass

		try:
			IP_index = fields.index("IP_vector")
			IP_vector_list = self.get_regex_vector("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
			fields.remove("IP_vector")
		except ValueError:
			pass

		try:
			Phone_index = fields.index("Phone_vector")
			Phone_vector_list = self.get_regex_vector("^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$")
			fields.remove("Phone_vector")
		except ValueError:
			pass

		try:
			URL_index = fields.index("URL_vector")
			URL_vector_list = self.get_regex_vector("^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?")
			fields.remove("URL_vector")
		except ValueError:
			pass

		search = "q=" + search
		field_builder = ""
		for field in fields:
			field_builder = field_builder + "," + field
		field_builder = "select?fl=" + field_builder + "&"
		query_builder = field_builder + search + "&wt=csv"
		query_builder = self.base_url + query_builder
		
		response = urllib2.urlopen(query_builder)

		if (response.code != 200):
			print("Error in solr query.\nPlease check fields and regex")
		else:
			to_return = []
			output = []
			for line in response:
				output.append(line)
			output = output[1:]
			counter = 0
			for element in output:
				element = element.split(",\"")
				values = []
				for value in element:
					if value.count(",") == 1:
						value = value.split(",",1)
						for word in value:
							word = word.strip("\n")
							values.append(word)
					else:
						value = value.strip("\n")
						value = value.strip("\"")
						values.append(value)
				if perm_index != -1:
					values.insert(perm_index, permissions_vector_list[counter])
				if sys_index != -1:
					values.insert(sys_index, sys_cmd_vector_list[counter])
				if IP_index != -1:
					values.insert(IP_index, IP_vector_list[counter])
				if Phone_index != -1:
					values.insert(Phone_index, Phone_vector_list[counter])
				if URL_index != -1:
					values.insert(URL_index, URL_vector_list[counter])
				to_return.append(values)
				counter = counter + 1
			if perm_index != -1:
				fields.insert(perm_index, "permissions_vector")
			if sys_index != -1:
				fields.insert(sys_index, "sys_cmd_vector")
			if IP_index != -1:
				fields.insert(IP_index, "IP_vector")
			if Phone_index != -1:
				fields.insert(Phone_index, "Phone_vector")
			if URL_index != -1:
				fields.insert(URL_index, "URL_vector")
			return to_return

	def get_permissions_vector(self, app_name="", version=""):
		response_list = []
		search = "*" + app_name + "*" + version + "*"
		field = "app_version,permissions"
		return_type = "csv"
		query = self.base_url + "select?fl=" + field + "&" + "q=" + search + "&wt=" + return_type
		response = urllib2.urlopen(query)
		for line in response:
			response_list.append(line)
		response_list = response_list[1:]
		solr_permissions_list = []
		for app in response_list:
			permissions = app.split(",",1)[1]
			permissions = permissions.strip("\"")
			permissions = permissions[:-2]
			solr_permissions_list.append(permissions.split(","))		
		android_permissions_list = []
		f = open(variables.permissions_list,"r")
		for line in f:
			line = line.strip("\n")
			android_permissions_list.append(line)
		f.close()
		android_permissions_list.sort()
		feature_vector_list = []
		for perm_list in solr_permissions_list:
			perm_list.sort()
			feature_vector = ""
			for permission in android_permissions_list:
				try:
					perm_list.index(permission)
					feature_vector = feature_vector + '1'
				except ValueError:
					feature_vector = feature_vector + '0'
			feature_vector_list.append(feature_vector)
		return feature_vector_list
		
	def get_regex_vector(self, reg, app_name="", version=""):
		response_list = []
		search = "*" + app_name + "*" + version + "*"
		field = "app_version,strings"
		return_type = "csv"
		query = self.base_url + "select?fl=" + field + "&" + "q=" + search + "&wt=" + return_type
		response = urllib2.urlopen(query)
		for line in response:
			response_list.append(line)
		response_list = response_list[1:]
		strings_list = []
		for app in response_list:
			strings = app.split(",",1)[1]
			strings = strings.strip("\"")
			strings = strings[:-2]
			strings_list.append(strings.split(","))
		feature_vector_list = []
		for string_list in strings_list:
			feature_vector = ""
			for string in string_list:
				searchIP = re.search(reg, string)
				if searchIP:
					feature_vector = feature_vector + '1'
				else:
					feature_vector = feature_vector + '0'
			feature_vector_list.append(feature_vector)
		return feature_vector_list

	def get_sys_cmd_vector(self, app_name="", version=""):
		response_list = []
		search = "*" + app_name + "*" + version + "*"
		field = "app_version,strings"
		return_type = "csv"
		query = self.base_url + "select?fl=" + field + "&" + "q=" + search + "&wt=" + return_type
		response = urllib2.urlopen(query)
		for line in response:
			response_list.append(line)
		response_list = response_list[1:]
		strings_list = []
		for app in response_list:
			strings = app.split(",",1)[1]
			strings = strings.strip("\"")
			strings = strings[:-2]
			strings_list.append(strings.split(","))
		feature_vector_list = []
		android_sys_cmd_list = []
		f = open(variables.sys_cmd_list,"r")
		for line in f:
			line = line.strip("\n")
			android_sys_cmd_list.append(line)
		f.close()
		for string_list in strings_list:
			feature_vector = ""
			for string in string_list:
				for cmd in android_sys_cmd_list:
					if string.find(" " + cmd + " ") != -1 or string.startswith(cmd + " ") == True:
						feature_vector = feature_vector + '1'
						break
					elif android_sys_cmd_list[len(android_sys_cmd_list)-1] == cmd:
						feature_vector = feature_vector + '0'
			feature_vector_list.append(feature_vector)
		return feature_vector_list