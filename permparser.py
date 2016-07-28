from apk_parse.apk import *
import sys

class permparser:

	perm_list = []
	__APK = ""
	feature_vector = ""

	def __init__(self, APK):
		self.__APK = APK
		self.perm_exist = False
		self.perm_list = self.get_perm_list(APK)

	def get_perm_list(self, APK):
		apkf = APK(read(file), raw=True)
		return apkf.get_permissions()