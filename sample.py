import urllib2

host_port = "http://localhost:8080"

def call_and_print(url):
    doc = urllib2.urlopen(url)
    for line in doc:
        print(line)

#package_name and permissions with an output of a csv
pn_p_c = (host_port + '/solr/apps/select?'
                    'q=*:*&fl=package_name+permissions&wt=csv')

#package_name and permissions with an output of a json
pn_p_j = (host_port + '/solr/apps/select?'
                    'q=*:*&fl=package_name+permissions&wt=json')

#package_name and permissions with an output of a xml
pn_p_x = (host_port + '/solr/apps/select?'
                    'q=*:*&fl=package_name+permissions&wt=xml')

# complex query extracting package_name and permissions
# but only APK's containing the android.permission.CAMERA,
# omits the header, return type of a csv, and limits the
# response to just 2 rows
complex_q = (host_port + '/solr/apps/select?'
    'q=*.CAMERA&omitHeader=true&fl=package_name+permissions&rows=2&wt=csv')

print("====================================================")
print("CSV:")
print("====================================================")
call_and_print(pn_p_c)

print("====================================================")
print("JSON:")
print("====================================================")
call_and_print(pn_p_j)

print("====================================================")
print("XML:")
print("====================================================")
call_and_print(pn_p_x)

print("====================================================")
print("Complex:")
print("====================================================")
call_and_print(complex_q)
