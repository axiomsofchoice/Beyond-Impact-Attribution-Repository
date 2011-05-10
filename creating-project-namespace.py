### @export "imports"
import fluidinfo
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

# create a namespace
headers, response = fluidinfo.call('POST', '/namespaces/ianmulvany', {'name': 'biar', 'description': 'beyond impact attribution registry namespace'})

# set the permission on creation under that namespace
headers, response = fluidinfo.call('PUT', '/permissions/namespaces/ianmulvany/biar', {'policy': 'open', 'exceptions': []}, action="create")

print headers 
print response


