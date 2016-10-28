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
	response_list = response_list[0].lstrip('"')
	permissions = response_list
	perm_list = permissions.split('"',1)[0]
	perm_list = perm_list.split(',')
	for perm in perm_list:
		print(perm)
	print(len(perm_list))
get_permissions_vector()

"""
Output:
android.permission.ACCESS_COARSE_LOCATION
android.permission.ACCESS_FINE_LOCATION
android.permission.ACCESS_LOCATION_EXTRA_COMMANDS
android.permission.ACCESS_NETWORK_STATE
android.permission.WAKE_LOCK
android.permission.RECEIVE_BOOT_COMPLETED
android.permission.GET_ACCOUNTS
android.permission.WRITE_EXTERNAL_STORAGE
android.permission.INTERNET
android.permission.ACCESS_WIFI_STATE
android.permission.READ_PHONE_STATE
com.android.browser.permission.WRITE_HISTORY_BOOKMARKS
com.android.browser.permission.READ_HISTORY_BOOKMARKS
com.android.launcher.permission.INSTALL_SHORTCUT
com.android.launcher.permission.UNINSTALL_SHORTCUT
com.android.launcher.permission.READ_SETTINGS
com.htc.launcher.permission.READ_SETTINGS
com.motorola.launcher.permission.READ_SETTINGS
com.motorola.dlauncher.permission.READ_SETTINGS
com.fede.launcher.permission.READ_SETTINGS
com.lge.launcher.permission.READ_SETTINGS
org.adw.launcher.permission.READ_SETTINGS
com.motorola.launcher.permission.INSTALL_SHORTCUT
com.motorola.dlauncher.permission.INSTALL_SHORTCUT
com.lge.launcher.permission.INSTALL_SHORTCUT
25
"""
