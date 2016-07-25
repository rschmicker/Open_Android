import couchdb
import time

def main():
	c = couchdb.Server()
	db = c['open_android']

	#app = "Facebook"
	#app = "'" + app + "'"

	app_query = '''function(doc) {
	    if (doc.app_name) {
	        emit(doc.app_name);
	    }
	}'''

	version_query = '''function(doc) {
	    if (doc.version) {
	        emit(doc.version);
	    }
	}'''

	"""
	'''function(doc) {
	    if (doc.app_name == ''' + app + ''') {
	        emit(doc.app_name);
	    }
	}'''

	version_query = '''function(doc) {
	    if (doc.app_name == ''' + app + ''') {
	        emit(doc.version);
	    }
	}'''
	"""

	app_names = []
	versions = []
	for row in db.query(app_query):
		app_names.append(row.key)
	for row in db.query(version_query):
		versions.append(row.key)
	for i in range(len(app_names)):
		print("APP: " + app_names[i] + "\tVersion: " + versions[i])

start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))