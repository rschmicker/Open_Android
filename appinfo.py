import subprocess
import hashlib
import sys

class appinfo:

	__single_apk_dir = ""
	APK_name = ""
	APK_version = ""
	MD5 = ""
	SHA256 = ""

	def __init__(self, APK):
		self.__single_apk_dir = APK
		self.set_APK_info()
		self.set_MD5_hash()
		self.set_SHA256_hash()
		#self.toString()

	def set_APK_info(self):
		info_cmd = "aapt d badging " +  "'" + self.__single_apk_dir + "'"
		info_subp = subprocess.Popen(['/bin/sh', '-c', info_cmd], stdout=subprocess.PIPE)
		out = info_subp.communicate()[0]
		all_info = out.splitlines()
		for info in all_info:
			if info.find("versionName='") != -1:
				info = info.split("versionName='",1)[1]
				info = info.split("'")[0]
				self.APK_version = info
			if info.startswith("application-label:"):
				info = info.replace(" ", "_")
				info = info.split("'")[1]
				info = info.replace("/","_")
				info = info.replace("(","_")
				info = info.replace(")","_")
				self.APK_name = info

	def set_MD5_hash(self):
		hash_md5 = hashlib.md5()
		with open(self.__single_apk_dir, "rb") as f:
			for chunk in iter(lambda: f.read(4096), b""):
				hash_md5.update(chunk)
		self.MD5 = hash_md5.hexdigest()

	def set_SHA256_hash(self):
		hash_sha256 = hashlib.sha256()
		with open(self.__single_apk_dir, "rb") as f:
			for chunk in iter(lambda: f.read(4096), b""):
				hash_sha256.update(chunk)
		self.SHA256 = hash_sha256.hexdigest()

	def toString(self):
		print("APK:\t\t\t" + self.APK_name)
		print("Version:\t\t" + self.APK_version)
		print("MD5:\t\t\t" + self.MD5)
		print("SHA256:\t\t\t" + self.SHA256)