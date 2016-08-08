from couchdb_api import *
import hashlib

class couch_db:
	def __init__(self, a, p, i, s, ap, com):
		self.c = Couch("localhost")
		self.appinfo = a
		self.perms = p
		self.intents = i
		self.strings = s
		self.apis = ap
		self.com = com
		self.dump_data()

	def dump_data(self):
		app_id = hashlib.md5()
		app_id.update(self.appinfo.APK_name + self.appinfo.APK_version)
		app_id = app_id.hexdigest()
		print("App ID: " + str(app_id))
		data = {}
		data['app_name'] = self.appinfo.APK_name
		data['version'] = self.appinfo.APK_version
		data['SHA256'] = self.appinfo.SHA256
		data['MD5'] = self.appinfo.MD5
		data['permissions'] = self.perms.perm_list
		data['permissions_vector'] = self.perms.feature_vector
		data['intents'] = self.intents.intent_list
		data['smali'] = self.com.smali
		data['smali_classification'] = self.com.smali_classification
		data['strings'] = self.strings.all_strings
		data['has_ip'] = self.strings.has_IP_list
		data['has_url'] = self.strings.has_URL_list
		data['has_phone'] = self.strings.has_Phone_list
		data['has_sys_cmd'] = self.strings.has_Sys_Cmd_list
		data['apis'] = self.apis.api_list
		data['has_dynamic'] = self.apis.has_dynamic_list
		data['has_encryption'] = self.apis.has_encryption_list
		data['has_network'] = self.apis.has_network_list
		doc = json.dumps(data)

		self.c.saveDoc('open_android', doc, app_id)
		#self.c.openDoc('open_android', app_id)