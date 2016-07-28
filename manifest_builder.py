from apk_parse.apk import *
import os
import variables
directory = "/home/openandroid/Documents/apks/"
def get_APK_list(APK_dir):
		apks = []
		for root, dirs, files in os.walk(APK_dir, topdown=False):
			for name in files:
				if name.endswith(".apk"):
					apks.append(os.path.join(root, name))	  
		return apks
apk_list = get_APK_list(directory)
for file in apk_list:
	try:
		apkf = APK(read(file), raw=True)
		print(apkf.get_permissions())
		break
	except:
		print("Bad file: " + file)
		print("Deleting...")
		os.remove(file)
		continue
	#print(apkf.package)
	#print(apkf.file_md5)
	#print(apkf.get_androidversion_name())