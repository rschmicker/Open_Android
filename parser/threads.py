from appinfo import *
from stringparser import *
from apiparser import *
from intentparser import *
from process import *
import threading
from json_builder import *

class threads(threading.Thread):
	def __init__(self, apk, threadLock):
		threading.Thread.__init__(self)
		self.apk = apk
		self.threadLock = threadLock

	def run(self):
		try:
			a = appinfo(self.apk)
			i = intentparser(self.apk)
			com = Sample(self.apk)
			self.threadLock.acquire()
			s = stringparser(self.apk)
			ap = apiparser(self.apk)
			self.threadLock.release()
			#mongo_db(a, i, s, ap, com)
			j = json_builder(a, i, s, ap, com)
		except ValueError:
			pass
