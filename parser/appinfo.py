import hashlib
import os
from apk_parse.apk import *
import variables
import sys

class appinfo:

	file_name = ""
	apk_dir = ""
	APK_name = ""
	APK_version = ""
	MD5 = ""
	SHA256 = ""
	perm_list = []

	def __init__(self, APK):
		# Name, Version, MD5, SHA256
		self.file_name = APK.split("/")[-1]
		self.file_name = self.file_name.strip(".apk")
		self.apk_dir = APK
		self.apkf = self.extractor()
		self.set_APK_info()
		self.set_MD5_hash()
		self.set_SHA256_hash()

		# Permissions
		self.perm_exist = False
		self.perm_list = []
		self.set_perm_list()

	def extractor(self):
		try:
			return APK(read(self.apk_dir), raw=True)
		except:
			print("Bad file: " + self.apk_dir)
			#os.remove(file)
			os.rename(self.apk_dir, variables.bad_apk_dir + self.file_name)
			raise ValueError('Bad Zip File')

	def set_perm_list(self):
		self.perm_list = self.apkf.get_permissions()
		if len(self.perm_list) != 0:
			self.perm_exist = True

	def set_APK_info(self):
		try:
			self.APK_name = self.apkf.package
			self.APK_version = self.apkf.get_androidversion_name()
		except KeyError:
			print("ERROR: parsing package name or version name")
			pass

	def set_MD5_hash(self):
		self.MD5 = self.apkf.file_md5

	def set_SHA256_hash(self):
		hash_sha256 = hashlib.sha256()
		with open(self.apk_dir, "rb") as f:
			for chunk in iter(lambda: f.read(4096), b""):
				hash_sha256.update(chunk)
		self.SHA256 = hash_sha256.hexdigest()