import urllib2

def call_and_print(url):
    doc = urllib2.urlopen(url)
    for line in doc:
        print(line)

#package_name and permissions with an output of a csv
pn_p_c = "http://localhost:8080/solr/apps/select?q=*:*&fl=package_name+permissions&wt=csv"

#package_name and permissions with an output of a json
pn_p_j = "http://localhost:8080/solr/apps/select?q=*:*&fl=package_name+permissions&wt=json"

#package_name and permissions with an output of a xml
pn_p_x = "http://localhost:8080/solr/apps/select?q=*:*&fl=package_name+permissions&wt=xml"

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
