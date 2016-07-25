import subprocess
from controller import *
import threading
import time
import variables

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
	threadLock = threading.Lock()
	threads = []
	counter = 1
	for APK in APK_list:
		if len(threads) == variables.threads:
			print("Too many threads! wating to join...")
			for t in threads:
				t.join(360)
				if t.isAlive() == False:
					print("Joined!")
				else:
					print("Thread not joined!")
					continue
			print("Done joining threads! continuing...")
			del threads[:]
			break ##########################

		apk_thread = controller(APK_dir, APK, threadLock)
		apk_thread.start()
		threads.append(apk_thread)

		print(str(counter) + "/" + str(len(APK_list)))
		counter = counter + 1

start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))