### @export "imports"
import fluidinfo
import json
import os

### @export "fluid-login"
USERNAME = os.environ["FLUID_USERNAME"]
PASSWORD = os.environ["FLUID_PASSWORD"]

if not USERNAME:
    raise Exception("Please supply a fluid account username")

if not PASSWORD:
    raise Exception("Please supply a fluid account password")

fluidinfo.login(USERNAME, PASSWORD)

headers, response = fluidinfo.call('GET', "/users/%s" % USERNAME)
print response


### @export "create-named-object"
headers, response = fluidinfo.call('POST', "/about/mybook")
print "headers from creating named object:"
print headers
print "response from creating named object:"
for k, v in response.items():
    print k, ":", v

### @export "create-anonymous-object"
headers, response = fluidinfo.call('POST', '/objects/')
print "headers from creating anonymous object:"
print headers
print "response from creating anonymous object:"
for k, v in response.items():
    print k, ":", v

obj_id = response['id']
print obj_id

#parent_namespace = '/namespaces/ianmulvany'
#namespace_info = {
#    'name': 'biar',
#    'description': 'beyond impact attribution registry namespace'
#}
#fluidinfo.call('POST', parent_namespace, namespace_info)

#permission_space = '/permissions/namespaces/ianmulvany/biar'
#permission_info = {
#    'policy': 'open',
#    'exceptions': []
#}
#fluidinfo.call('PUT', permission_space, permission_info, action="create")


### @export "view-project-namespace"
parent_namespace = '/namespaces/biar'
headers, response = fluidinfo.call('GET', parent_namespace)

print headers
print response

### @export "create-biar-element-tag"
biar_namespace = '/tags/biar'
tag_info = {
    'name' : 'element',
    'description' : 'Tag indicating that object is part of BIAR',
    'indexed' : False
}
print "=================================================="
print biar_namespace
print tag_info
headers, response = fluidinfo.call('POST', biar_namespace, tag_info)
print headers
print response

### @export "link-object-to-biar"
object_tag_path = "/objects/%s/%s/%s" % (obj_id, 'biar', tag_info['name'])
print object_tag_path

headers, response = fluidinfo.call('PUT', object_tag_path)
print headers
print response

headers, response = fluidinfo.call('GET', "/objects/%s" % obj_id)
print headers
print response

headers, response = fluidinfo.call('GET', "/namespaces/biar", returnTags=True)
print headers
print response

headers, response = fluidinfo.call('GET', '/objects', query='has biar/element')
print headers
print response

parent_namespace = '/namespaces/biarcollections'
headers, response = fluidinfo.call('GET', parent_namespace)

print headers
print response

