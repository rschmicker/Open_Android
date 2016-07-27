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
import variables
from multiprocessing.dummy import Pool as ThreadPool

class controller:
	
	def __init__(self):
		self.apk_list = self.get_APK_list(variables.apk_dir)
		# synchronos threading
		self.sync_controller()
		
		# single threaded
		#for apk in self.apk_list:
		#	self.extractor(apk)
		
		# thread pool
		#self.threadPool(self.apk_list, variables.threads)

	def get_APK_list(self, APK_dir):
		apks = []
		for root, dirs, files in os.walk(APK_dir, topdown=False):
			for name in files:
				if name.endswith(".apk"):
					apks.append(os.path.join(root, name))	  
		return apks

	def sync_controller(self):
		threadLock = threading.Lock()
		threads_list = []
		self.counter = 1
		for APK in self.apk_list:
			if len(threads_list) == variables.threads:
				#print("Too many threads! wating to join...")
				for t in threads_list:
					t.join(360)
					#if t.isAlive() == False:
					#	print("Joined!")
					#else:
					#	print("Thread not joined!")
					#	continue
					self.completionRate()
				#print("Done joining threads! continuing...")
				del threads_list[:]

			apk_thread = threads(APK, threadLock)
			apk_thread.start()
			threads_list.append(apk_thread)
			self.counter = self.counter + 1


	def threadPool(self, apks, threads=2):
		pool = ThreadPool(threads)
		results = pool.map(self.extractor, apks)
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
		out = str(self.counter/len(self.apk_list)*100)+"%\t"+str(self.counter) + "/" + str(len(self.apk_list))
		sys.stdout.write('\r' + str(out) + ' ' * 20)
		sys.stdout.flush()