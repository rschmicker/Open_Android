#!/usr/bin/env python
import subprocess
import json
import re

json_loc = [
	("/home/openandroid/Documents/solr_json/wedplankit.iconosys.eng_fbc832ad575a43dceacb31c9f6c08597.json"),
	("/home/openandroid/Documents/solr_json/vbkoxh.cswnpr_06a64b522a7d715b9b59bd0eeb1c2d87.json"),
	("/home/openandroid/Documents/solr_json/vbkoxh.cswnpr_134fc1d516ee9840ea2dde563b126788.json"),
	("/home/openandroid/Documents/solr_json/vbkoxh.cswnpr_161341892b734f8d81eb7804f265ba7c.json"),
	("/home/openandroid/Documents/solr_json/vbkoxh.cswnpr_f6cd8a3d78864ec0248474bfd6252004.json"),
	("/home/openandroid/Documents/solr_json/vbkoxh.cswnpr_f4689de66672be6297f83e6f771f7b9f.json"),
	("/home/openandroid/Documents/solr_json/ru.install.opera_91c5226569950e77529633cdf60ff674.json"),
	("/home/openandroid/Documents/solr_json/rrreh.nyur_4549f544b6dcdd3104aa44930b9ea399.json"),
	("/home/openandroid/Documents/solr_json/rom.jonas.eley_a88379ac2400346715ad546b5ec09c65.json"),
	("/home/openandroid/Documents/solr_json/qq.tencent_a26b8936fdeb9c882e3827005f7b9a66.json"),
	("/home/openandroid/Documents/solr_json/pushme.android_c4967bd52e88d9d19a3efff2b33daa84.json"),
	("/home/openandroid/Documents/solr_json/org.tig.gqek_1ec2b89b8220c88bb8317a74b9e47ec6.json"),
	("/home/openandroid/Documents/solr_json/org.netraffic_72453fc8e1d988811db5003e16fa6a68.json"),
	("/home/openandroid/Documents/solr_json/org.expressme.love.ui_d25008db2e77aae53aa13d82b20d0b6a.json"),
	("/home/openandroid/Documents/solr_json/org.drhu.solarsystem_f4e0f47da0796986657fcf9afef747f3.json"),
	("/home/openandroid/Documents/solr_json/org.android.system_a290248b0f34c876bd0c01475b401ec8.json"),
	("/home/openandroid/Documents/solr_json/km.home_068d2eb945607caffb62e7e1512160e5.json"),
	("/home/openandroid/Documents/solr_json/jp.waraerudouga_857ee29d88796e1f1b7b440dc9eadc77.json"),
	("/home/openandroid/Documents/solr_json/Jk7H.PwcD_fe8308995762bceb741a379a05b55f13.json"),
	("/home/openandroid/Documents/solr_json/Jk7H.PwcD_993cda7aa4ff3afc205853365b72ab06.json"),
]
for loc in json_loc:
	with open(loc) as data_file:
		data = json.load(data_file)

	name = data['package_name']
	version = data['version']
	apis = data['apis']
	strings = data['strings']
	intents = data['intents']
	smali = data['smali']
	smali_class = data['smali_classification']
	md5 = data['MD5']
	sha2 = data['SHA256']

	query1 = "http://localhost:8080/solr/apps/select?q=MD5:"
	query2 = md5
	query3 = "&wt=json"

	solr = "curl '" + query1 + query2 + query3 + "'"
	solr_request = subprocess.Popen(['/bin/sh', '-c', solr], stdout=subprocess.PIPE)
	out = solr_request.communicate()[0]


	searchObj = re.search(name, out)
	if(searchObj):
		print("Name: " + name + " found")
	else:
		print("Name: " + name + " not found")

	searchObj = re.search(version, out)
	if(searchObj):
        	print("Version: " + version + " found")
	else:
        	print("Version: " + version + " not found")

	for line in apis:
		searchObj = re.search(re.escape(line), out)
		if(searchObj):
			print("API: " + line + " found")
		else:
			print("API " + line + " not found")
			break

	for line in strings:
		if(line.encode("utf-8") == ""):
			continue
		if(out.find(line.encode("utf-8"))):
                	print("String: " + line + " found")
        	else:
                	print("String: " + line + " not found")
                	break

	for line in smali:
        	if(line.encode("utf-8") == ""):
                	continue
        	if(out.find(line.encode("utf-8"))):
                	print("Smali: " + line + " found")
        	else:
                	print("Smali: " + line + " not found")
                	break

	for line in smali_class:
        	if(line.encode("utf-8") == ""):
                	continue
        	if(out.find(line.encode("utf-8"))):
                	print("Smali_class: " + line + " found")
        	else:
                	print("Smali_class: " + line + " not found")
                	break

	searchObj = re.search(md5, out)
	if(searchObj):
        	print("MD5: " + md5 + " found")
	else:
        	print("MD5: " + md5 + " not found")

	searchObj = re.search(sha2, out)
	if(searchObj):
        	print("Name: " + sha2 + " found")
	else:
        	print("Name: " + sha2 + " not found")
