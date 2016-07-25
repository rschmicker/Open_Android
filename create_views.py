import couchdb
from couchdb_api import *



c = Couch("localhost")
c.connect()
data = """
{
	"_rev":"A00",
	"language":"javascript",
	"views":
	{
		"all_perms": {
			"map": "function(doc){ if (doc.permissions) emit(doc.app_name, doc.permissions)}"
		},
		"all_perm_vectors":{
			"map": "function(doc){ if(doc.permissions_vector) emit(doc.app_name, doc.permissions_vector)}"
		},
		"all_version": {
			"map": "function(doc){ if(doc.version) emit(doc.app_name, doc.version)}"
		},
		"all_SHA256": {
			"map": "function(doc){ if(doc.SHA256) emit(doc.app_name, doc.SHA256)}"
		},
		"all_MD5": {
			"map": "function(doc){ if(doc.MD5) emit(doc.app_name, doc.MD5)}"
		},
		"all_intents": {
			"map": "function(doc){ if(doc.intents) emit(doc.app_name, doc.intents)}"
		},
		"all_smali": {
			"map": "function(doc){ if(doc.smali && doc.smali_classification) emit(doc.app_name, doc.smali, doc.smali_classification)}"
		},
		"all_strings": {
			"map": "function(doc){ if(doc.strings) emit(doc.app_name, doc.strings)}"
		},
		"all_has_ip": {
			"map": "function(doc){ if(doc.has_ip) emit(doc.app_name, doc.has_ip)}"
		},
		"all_has_url": {
			"map": "function(doc){ if(doc.has_url) emit(doc.app_name, doc.has_url)}"
		},
		"all_has_phone": {
			"map": "function(doc){ if(doc.has_phone) emit(doc.app_name, doc.has_phone)}"
		},
		"all_has_sys_cmd": {
			"map": "function(doc){ if(doc.has_sys_cmd) emit(doc.app_name, doc.has_sys_cmd)}"
		},
		"all_apis": {
			"map": "function(doc){ if(doc.apis) emit(doc.app_name, doc.apis)}"
		},
		"all_has_dynamic": {
			"map": "function(doc){ if(doc.has_dynamic) emit(doc.app_name, doc.has_dynamic)}"
		},
		"all_has_encryption": {
			"map": "function(doc){ if(doc.has_encryption) emit(doc.app_name, doc.has_encryption)}"
		},
		"all_has_network": {
			"map": "function(doc){ if(doc.has_network) emit(doc.app_name, doc.has_network)}"
		}
	}

}
"""
doc = json.dumps(data)
print(doc)

c.saveDoc("open_android", doc, "by_permissions")
#c.saveDoc('open_android', doc, app_id)
#c.openDoc("open_android", "ff04f1f3499e467b2ef9a2d61f06a9bd")
"""
{
  "_id":"_design/company",
  "_rev":"12345",
  "language": "javascript",
  "views":
  {
    "all": {
      "map": "function(doc) { if (doc.Type == 'customer')  emit(null, doc) }"
    },
    "by_lastname": {
      "map": "function(doc) { if (doc.Type == 'customer')  emit(doc.LastName, doc) }"
    },
    "total_purchases": {
      "map": "function(doc) { if (doc.Type == 'purchase')  emit(doc.Customer, doc.Amount) }",
      "reduce": "function(keys, values) { return sum(values) }"
    }
  }
}

"""
"""
class Connect():
	def __init__(self, user, password, dbname = "open_android",host="localhost", port=5984, options=None):
		self.host = host
		self.port = port
		self.user = user
		self.password = password
		self.dbname = dbname
		self.url = "http://"+self.host+":"+str(self.port)+"/"
		self.cnx = couchdb.Server(self.url)
		self.cnx.resource.credentials = (self.user, self.password)
		self.db = self.cnx[self.dbname]

	def get_app_name(self, app="all"):
		if app != "all":
			app_query = '''
				function(doc) {
	    			if(doc.app_name == ''' + app + ''') {
	        			emit(doc.app_name);
	    			}
				}'''			
		else:
			app_query = '''
				function(doc) {
	    			if(doc.app_name) {
	        			emit(doc.app_name);
	    			}
				}'''
		app_name = []
		for row in self.db.query(app_query):
			app_names.append(row.key)
		return app_name

	def get_app_perm(self, app="all"):
		perms = {}
		if app != "all":
			perm_query = '''
				function(doc){
					if(doc.app_name == ''' + app + '''){
						if(doc.permissions){
							emit(doc.app_name, doc.permissions)
						}
					}
				}
			'''
		else:
			perm_query = '''
				function(doc){					
					if(doc.permissions){
						emit(doc.app_name, doc.permissions)
					}
				}
			'''
		perm_list = []
		for row in self.db.query(perm_query):
			perm_list.append(row.key)
		return perm_list

	def get_app_perm_vector(self, app="all"):
		if app != "all":
			perm_query = '''
				function(doc){
					if(doc.app_name == ''' + app + '''){
						if(doc.permissions){
							emit(doc.app_name, doc.permissions)
						}
					}
				}
			'''
		else:
			perm_query = '''
				function(doc){					
					if(doc.permissions){
						emit(doc.app_name, doc.permissions)
					}
				}
			'''



		
c = Connect("rschmicker", "unhcfreg")
test = c.get_app_perm()
print(test)
"""
