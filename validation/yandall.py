#!/usr/bin/env python
import urllib2
import json

def get_permissions_vector():
	query = "http://localhost:8080/solr/apps/select?q=*org.drhu.solarsystem*&omitHeader=true&fl=permissions+apis+strings+package_name+version&wt=csv"
	response_list = []
	response = urllib2.urlopen(query)
	for line in response:
		response_list.append(line)
	response_list = response_list[1:]
	
	#permissions
	permissions = response_list[0].lstrip('"')
	perm_list = permissions.split('"',1)[0]
	perm_list = perm_list.split(',')
	for perm in perm_list:
		print(perm)
	
	#apis
	apis = response_list[0].split('"')[3]
	print(apis)	

	#sys commands
	response_list = []
        search = "*org.drhu.solarsystem*"
        field = "package_name,strings"
        return_type = "csv"
        query = "http://localhost:8080/solr/apps/select?fl=" + field + "&" + "q=" + search + "&wt=" + return_type
        response = urllib2.urlopen(query)
        for line in response:
                response_list.append(line)
        response_list = response_list[1:]
        string_list = []
        string_list = response_list[0].split(',',1)[1]
        string_list = string_list.split(',')
	android_sys_cmd_list = []
        f = open("sys_cmd_list.txt","r")
        for line in f:
        	line = line.strip("\n")
                android_sys_cmd_list.append(line)
        f.close()
        feature_vector = ""
        for string in string_list:
                for cmd in android_sys_cmd_list:
                        if string.find(" " + cmd + " ") != -1 or string.startswith(cmd + " ") == True:
                                feature_vector = feature_vector + '1'
                                break
                        elif android_sys_cmd_list[len(android_sys_cmd_list)-1] == cmd:
                                feature_vector = feature_vector + '0'
	print(feature_vector)
get_permissions_vector()

