#!/usr/bin/env python3
import io
import json
import sys
import re

# Query
# curl "http://localhost:8080/solr/apps/select?q=*:*&fl=package_name+MD5+strings+malicious&wt=json&rows=7000" > output.json

f = open("ips.txt",'w')

with open('output.json', encoding='utf-8') as data_file:
    data = json.loads(data_file.read())

pat = re.compile("^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")
f.write("Malicious PackageName MD5 IP\n")
for i in range(0, 7000):
	try:
		for line in data['response']['docs'][i]['strings']:
			if pat.search(line) is not None:
				f.write(str(data['response']['docs'][i]['malicious']) + " " + str(data['response']['docs'][i]['package_name']) + " " + str(data['response']['docs'][i]['MD5']) + " " + line + "\n")
	except KeyError as e:
		print("skip")

f.close()
