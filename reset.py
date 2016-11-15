import urllib2
import subprocess
from pymongo import MongoClient
response = urllib2.urlopen("http://localhost:8983/solr/apps/update?stream.body=%3Cdelete%3E%3Cquery%3E*:*%3C/query%3E%3C/delete%3E&commit=true")
