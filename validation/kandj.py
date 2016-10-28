#!/usr/bin/env python
import urllib2
import json

def get_permissions_vector():
	query = "http://localhost:8080/solr/apps/select?q=*org.drhu.solarsystem*&omitHeader=true&fl=permissions+package_name+version&wt=csv"
	response_list = []
	response = urllib2.urlopen(query)
	for line in response:
		response_list.append(line)
	response_list = response_list[1:]
	solr_permissions_list = []
	permissions = response_list[0]
	perm_list = permissions.split(',')	
	android_permissions_list = []
	f = open("permissions_list.txt","r")
	for line in f:
		line = line.strip("\n")
		android_permissions_list.append(line)
	f.close()
	android_permissions_list.sort()
	feature_vector = ""
	for permission in android_permissions_list:
		try:
			perm_list.index(permission)
			feature_vector = feature_vector + '1'
		except ValueError:
			feature_vector = feature_vector + '0'
	print(feature_vector)
	print(len(perm_list))
get_permissions_vector()

"""
Output:
0011010100000000000000000000000000000000000000010000000010000000000000000000010000000100000000000000000000000000000100001000000000011
27
"""
