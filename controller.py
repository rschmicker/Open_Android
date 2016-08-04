from permparser import *
from appinfo import *
from stringparser import *
from apiparser import *
from intentparser import *
from process import *
from threads import *
import threading
from mongo_db import *
from json_builder import *
from solr_api import *
import sys
import os
import variables
from multiprocessing.dummy import Pool as ThreadPool

class controller:
	
	def __init__(self):
		self.apk_list = self.get_APK_list(variables.apk_dir)

		# thread pool
		#self.threadPoolDecode(self.apk_list, variables.threads)

		# synchronos threading
		self.sync_controller()
		
		# single threaded
		#for apk in self.apk_list:
		#	self.extractor(apk)
		
		

	def get_APK_list(self, APK_dir):
		apks = []
		for root, dirs, files in os.walk(APK_dir, topdown=False):
			for name in files:
				if name.endswith(".apk"):
					a = appinfo(os.path.join(root, name))
					apk_name = a.APK_name
					MD5 = a.MD5
					mongo_fname = variables.mongo_json + apk_name + "_" + MD5 + '.json'
					solr_fname = variables.json_dir + apk_name + "_" + MD5 + '.json'
					if os.path.isfile(mongo_fname) and os.path.isfile(solr_fname):
						print("Skipping:\t" + os.path.join(root, name))
						continue
					else:
						print("Appending:\t" + os.path.join(root, name))
						apks.append(os.path.join(root, name))	  
		return apks

	def decode(self, apk):
		out_apk = apk.strip(".apk")
		out_apk = out_apk.split("/")[-1]
		out_folder = variables.decoded_apk_dir + out_apk
		decode_cmd = "./apktool.sh d --quiet -o '" + out_folder + "' '" + apk + "'"
		decode_subp = subprocess.Popen(['/bin/sh', '-c', decode_cmd], stdout=subprocess.PIPE)
		out = decode_subp.communicate()[0]

	def sync_controller(self):
		threadLock = threading.Lock()
		threads_list = []
		self.counter = 1
		for APK in self.apk_list:
			if len(threads_list) == variables.threads:
				for t in threads_list:
					t.join(360)
					self.completionRate()
				del threads_list[:]
				#break
			self.completionRate()
			apk_thread = threads(APK, threadLock)
			if self.counter == 175:
				os.execl(sys.executable, sys.executable, *sys.argv)
			else:
				self.counter = self.counter + 1
			apk_thread.start()
			threads_list.append(apk_thread)


	def threadPoolDecode(self, apks, threads=2):
		pool = ThreadPool(threads)
		results = pool.map(self.decode, apks)
		pool.close()
		pool.join()
		return results
		
	def async_extractor(self, apk):
		a = appinfo(apk)
		p = permparser(apk)
		i = intentparser(apk)
		com = Sample(apk)
		s = stringparser(apk)
		ap = apiparser(apk)
		mongo_db(a, p, i, s, ap, com)
		j = json_builder(a, p, i, s, ap, com)

	def completionRate(self):
		out = str(self.counter) + "/" + str(len(self.apk_list))
		sys.stdout.write('\r' + str(out) + ' ' * 20)
		sys.stdout.flush()