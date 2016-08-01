import variables
import subprocess

def get_APK_list(APK_dir):
		apks = []
		for root, dirs, files in os.walk(APK_dir, topdown=False):
			for name in files:
				if name.endswith(".apk"):
					apks.append(os.path.join(root, name))	  
		return apks

apks = get_APK_list(variables.apk_dir)

for path in apks:
	out_folder = variables.decoded_apk_dir + apk_name
	decode_cmd = "./apktool.sh d --quiet -o '" + out_folder + "' '" + path + "'"
	decode_subp = subprocess.Popen(['/bin/sh', '-c', decode_cmd], stdout=subprocess.PIPE)
	out = decode_subp.communicate()[0]