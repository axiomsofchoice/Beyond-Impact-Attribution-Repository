### @export "imports"
import fluidinfo
import json
import os
import urllib

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

#http://www.archive.org/details/ste-531
