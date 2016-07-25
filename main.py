import subprocess
import controller
import threading
import time
import variables
from multiprocessing.dummy import Pool as ThreadPool

def get_APK_list(APK_dir):
		list_apk_cmd = "ls " + APK_dir + " | grep .apk"
		list_subp = subprocess.Popen(['/bin/sh', '-c', list_apk_cmd], stdout=subprocess.PIPE)
		out = list_subp.communicate()[0]
		apk_list = []
		for line in out.splitlines():
			if line.find(" ") != -1:
				line = "'" + line + "'"
				apk_modify = "mv " + APK_dir + line + " " + APK_dir + line.replace(" ","_")
				list_subp = subprocess.Popen(['/bin/sh', '-c', apk_modify], stdout=subprocess.PIPE)
				line = line.replace(" ","_")
			apk_list.append(line)
		return apk_list

def main():
	APK_dir = variables.apk_dir
	APK_list = get_APK_list(APK_dir)
	for i in range(len(APK_list)):
		APK_list[i] = APK_dir + APK_list[i]

	output = controller.threadPool(APK_list, 4)
	print(output)


start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))