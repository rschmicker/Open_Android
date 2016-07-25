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
from multiprocessing.dummy import Pool as ThreadPool

class controller:
    completed_apks = []
    def __init__(self):
        self.apk_list = self.get_APK_list(variables.apk_dir)
        self.threadPool(self.apk_list, 4)

    def get_APK_list(self, APK_dir):
        apks = []
        for root, dirs, files in os.walk(APK_dir, topdown=False):
            for name in files:
                if name.endswith(".apk"):
                    apks.append(os.path.join(root, name))      
        return apks

    def threadPool(self, apks, threads=2):
        pool = ThreadPool(threads)
        results = pool.map(self.extractor, apks)
        pool.close()
        pool.join()
        return results
        
    def extractor(self, apk):
        a = appinfo(apk)
        p = permparser(apk)
        i = intentparser(apk)
        com = Sample(apk)
        s = stringparser(apk)
        ap = apiparser(apk)
        mongo_db(a, p, i, s, ap, com)
        j = json_builder(a, p, i, s, ap, com)
        self.completed_apks.append(a.APK_name)
        self.completionRate()

    def completionRate(self):
        print(str(len(self.completed_apks)/len(self.apk_list)*100) + "%")