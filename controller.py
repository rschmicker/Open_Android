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


def threadPool(apks, threads=2):
    pool = ThreadPool(threads)
    results = pool.map(extractor, apks)
    pool.close()
    pool.join()
    return results
    
def extractor(apk):
    a = appinfo(apk)
    p = permparser(apk)
    i = intentparser(apk)
    com = Sample(apk)
    s = stringparser(apk)
    ap = apiparser(apk)
    mongo_db(a, p, i, s, ap, com)
    j = json_builder(a, p, i, s, ap, com)