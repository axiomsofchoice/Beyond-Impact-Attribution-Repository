### @export "imports"
import fluidinfo
import json
import os
import urllib

### @export "fluid-login"
USERNAME = 'biar'
PASSWORD = 'beyondimpact'

if not USERNAME:
    raise Exception("Please supply a fluid account username")

if not PASSWORD:
    raise Exception("Please supply a fluid account password")

fluidinfo.login(USERNAME, PASSWORD)

headers, response = fluidinfo.call('GET', "/users/%s" % USERNAME)
print response

### @export "set-namespace-permissions"
permission_space = '/permissions/namespaces/biar'
permission_info = {
    'policy': 'closed',
    'exceptions': ['birukou', 'ianmulvany', 'axiomsofchoice', 'svanderwaal', 'ananelson', 'biar']
}
fluidinfo.call('PUT', permission_space, permission_info, action="create")
print headers
print response
fluidinfo.call('PUT', permission_space, permission_info, action="update")
print headers
print response
fluidinfo.call('PUT', permission_space, permission_info, action="delete")
print headers
print response
fluidinfo.call('PUT', permission_space, permission_info, action="list")
print headers
print response
fluidinfo.call('PUT', permission_space, permission_info, action="control")
print headers
print response

### @end

