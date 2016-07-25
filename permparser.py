import subprocess
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
		aapt_cmd = "aapt d permissions "
		perm_list = []
		perm_cmd = aapt_cmd + "'" + APK + "'"
		perm_subp = subprocess.Popen(['/bin/sh', '-c', perm_cmd], stdout=subprocess.PIPE)
		out = perm_subp.communicate()[0]
		temp_list = out.splitlines()
		for string in temp_list:
			if string.startswith("permission: "):
				temp = string[12:]
			else:
				temp = string[string.find("'")+1:-1]
			if string.find("package:") != -1:
				continue
			perm_list.append(temp)
		if len(perm_list) != 0:
			self.perm_exist = True
		return perm_list

	def toString(self):
		print("All Requested Permissions:")
		for permission in self.perm_list:
			print("\t" + permission)
		print("Feature vector: ")
		print(self.feature_vector)