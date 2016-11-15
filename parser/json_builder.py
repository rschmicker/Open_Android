import json
import variables

class json_builder:
	def __init__(self, a, i, s, ap, com):
		self.appinfo = a
		self.intents = i
		self.strings = s
		self.apis = ap
		self.com = com
		self.output = variables.json_dir + self.appinfo.APK_name + "_" + self.appinfo.MD5 + '.json'
		self.toJson()

	def toJson(self):
		data = {}
		data['package_name'] = self.appinfo.APK_name
		data['version'] = str(self.appinfo.APK_version)
		data['SHA256'] = self.appinfo.SHA256
		data['MD5'] = self.appinfo.MD5
		if(self.appinfo.apk_dir.find("malware")==-1):
			data['malicious'] = False
		else:		
			data['malicious'] = True
		data['permissions'] = self.appinfo.perm_list
		data['intents'] = self.intents.intent_list
		data['smali'] = self.com.smali
		data['smali_classification'] = self.com.smali_classification
		data['strings'] = self.strings.all_strings
		data['apis'] = self.apis.api_list
		with open(self.output, 'w') as outfile:
			json.dump(data, outfile, indent=4, sort_keys=True, separators=(',', ':'))

	def toSolr(self):
		solr_cmd = variables.solr_dir + 'bin/post -c ' + variables.solr_collection_name + ' ' + variables.json_dir + self.appinfo.APK_name + '.json'
		solr_subp = subprocess.Popen(['/bin/sh', '-c', solr_cmd], stdout=subprocess.PIPE)
		out = solr_subp.communicate()[0]
