from permparser import *
from appinfo import *
from stringparser import *
from apiparser import *
from intentparser import *
from process import *
import threading
from mongo_db import *
from json_builder import *
from solr_api import *

class controller(threading.Thread):
    def __init__(self, APK_dir, APK, threadLock):
        threading.Thread.__init__(self)
        self.APK_dir = APK_dir
        self.APK = APK
        self.threadLock = threadLock
    def run(self):
        a = appinfo(self.APK_dir + self.APK)
        p = permparser(self.APK_dir + self.APK)
        i = intentparser(self.APK_dir + self.APK)
        com = Sample(self.APK_dir + self.APK)
        self.threadLock.acquire()
        s = stringparser(self.APK_dir + self.APK)
        ap = apiparser(self.APK_dir + self.APK)
        self.threadLock.release()
        mongo_db(a, p, i, s, ap, com)
        j = json_builder(a, p, i, s, ap, com)