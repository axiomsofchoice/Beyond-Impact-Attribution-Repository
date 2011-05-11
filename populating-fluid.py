### @export "imports"
import fluidinfo
import json
import os
import pprint

pp = pprint.PrettyPrinter(indent=4)

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
pp.pprint(headers)
print "response from creating named object:"
pp.pprint(response)

### @export "create-anonymous-object"
headers, response = fluidinfo.call('POST', '/objects/')
print "headers from creating anonymous object:"
pp.pprint(headers)
print "response from creating anonymous object:"
pp.pprint(response)

obj_id = response['id']
print obj_id

### @export "legacy-permissions"

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
pp.pprint(headers)
pp.pprint(response)

### @export "create-biar-element-tag"
#biar_namespace = '/tags/biar'
#tag_info = {
#    'name' : 'element',
#    'description' : 'Tag indicating that object is part of BIAR',
#    'indexed' : False
#}
#headers, response = fluidinfo.call('POST', biar_namespace, tag_info)
#print headers
#print response

### @export "view-biar-element-tag"
headers, response = fluidinfo.call('GET', '/tags/biar/element')
pp.pprint(headers)
pp.pprint(response)

### @export "list-all-biar-elements"
headers, response = fluidinfo.call('GET', '/objects', query='has biar/element')
pp.pprint(headers)
pp.pprint(response)

### @export "create-parent-namespaces"
list_parent_namespace = '/namespaces'
namespace_info = {
    'name': 'ananelson',
    'description': 'personal namespace'
}
headers, response = fluidinfo.call('POST', list_parent_namespace, namespace_info)

list_parent_namespace = '/namespaces/ananelson'
namespace_info = {
    'name': 'biar',
    'description': 'place to put biar stuff'
}
headers, response = fluidinfo.call('POST', list_parent_namespace, namespace_info)

list_parent_namespace = '/namespaces/ananelson/biar'
namespace_info = {
    'name': 'collections',
    'description': 'biar collections'
}
headers, response = fluidinfo.call('POST', list_parent_namespace, namespace_info)

### @export "create-collections"
list_parent_namespace = '/namespaces/ananelson/biar/collections'
namespace_info = {
    'name': 'myfirstlist',
    'description': 'my phd reading list'
}
headers, response = fluidinfo.call('POST', list_parent_namespace, namespace_info)
pp.pprint(headers)
pp.pprint(response)

list_parent_namespace = '/namespaces/ananelson/biar/collections'
namespace_info = {
    'name': 'mysecondlist',
    'description': 'bedtime reading list'
}
headers, response = fluidinfo.call('POST', list_parent_namespace, namespace_info)
pp.pprint(headers)
pp.pprint(response)

### @export "create-list-element-tag"
tag_info = {
    'name' : 'element',
    'description' : 'Tag indicating that object is part of a list',
    'indexed' : False
}
user_biar_namespace = '/tags/ananelson/biar/collections/myfirstlist'
headers, response = fluidinfo.call('POST', user_biar_namespace, tag_info)
pp.pprint(headers)
pp.pprint(response)

user_biar_namespace = '/tags/ananelson/biar/collections/mysecondlist'
headers, response = fluidinfo.call('POST', user_biar_namespace, tag_info)
pp.pprint(headers)
pp.pprint(response)

### @export "create-list-rating-tag"
tag_info = {
    'name' : 'rating',
    'description' : 'Assign a rating in the context of a list',
    'indexed' : False
}
user_biar_namespace = '/tags/ananelson/biar/collections/myfirstlist'
headers, response = fluidinfo.call('POST', user_biar_namespace, tag_info)
pp.pprint(headers)
pp.pprint(response)

user_biar_namespace = '/tags/ananelson/biar/collections/mysecondlist'
headers, response = fluidinfo.call('POST', user_biar_namespace, tag_info)
pp.pprint(headers)
pp.pprint(response)

### @export "element-in-list"
object_tag_path = "/objects/%s/%s/%s" % (obj_id, 'ananelson/biar/collections/myfirstlist', 'element')

headers, response = fluidinfo.call('PUT', object_tag_path)
pp.pprint(headers)
pp.pprint(response)

### @export "query-list"
headers, response = fluidinfo.call('GET', '/objects', query='has ananelson/biar/collections/myfirstlist/element')
pp.pprint(headers)
pp.pprint(response)

### @export "assign-rating-in-list"
object_tag_path = "/objects/%s/%s/%s" % (obj_id,
                                         'ananelson/biar/collections/myfirstlist',
                                         'rating')
print object_tag_path

headers, response = fluidinfo.call('PUT', object_tag_path, 6)
print headers
print response

object_tag_path = "/objects/%s/%s/%s" % (obj_id, 'ananelson/biar/collections/mysecondlist', 'element')
print object_tag_path

headers, response = fluidinfo.call('PUT', object_tag_path)
print headers
print response

### @export "assign-rating-in-list"
object_tag_path = "/objects/%s/%s/%s" % (obj_id,
                                         'ananelson/biar/collections/mysecondlist',
                                         'rating')
print object_tag_path

headers, response = fluidinfo.call('PUT', object_tag_path, 2)
print headers
print response





#headers, response = fluidinfo.call('GET', "/objects/%s" % obj_id)
#print headers
#print response
#
#headers, response = fluidinfo.call('GET', "/namespaces/biar", returnTags=True)
#print headers
#print response
#
#
#
#headers, response = fluidinfo.call('GET', '/objects', query='biar/collection matches "myfirstlist"')
#print headers
#print response
#
#headers, response = fluidinfo.call('GET', '/objects', query='biar/collection matches "mysecondlist"')
#print headers
#print response

#parent_namespace = '/namespaces/biarcollections'
#headers, response = fluidinfo.call('GET', parent_namespace)
#print headers
#print response


