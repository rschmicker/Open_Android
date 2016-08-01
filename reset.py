import urllib2
import subprocess
from pymongo import MongoClient
response = urllib2.urlopen("http://localhost:8983/solr/apps/update?stream.body=%3Cdelete%3E%3Cquery%3E*:*%3C/query%3E%3C/delete%3E&commit=true")

client = MongoClient(host="localhost",port=27017)
client.drop_database("open_android")

#cmd = "rm -rf /home/openandroid/Documents/decodedapks/* && rm /home/openandroid/Documents/mongo_json/* && rm /home/openandroid/Documents/solr_json/*"
#subp = subprocess.Popen(['/bin/sh', '-c', cmd], stdout=subprocess.PIPE)
#out = subp.communicate()[0]
#print(out)