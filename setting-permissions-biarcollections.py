### @export "imports"
import fluidinfo
import json
import os
import urllib

### @export "fluid-login"
USERNAME = 'biarcollections'
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
    'exceptions': ['biar','birukou', 'ianmulvany', 'axiomsofchoice', 'svanderwaal', 'ananelson']
}
fluidinfo.call('PUT', permission_space, permission_info, action="create")
fluidinfo.call('PUT', permission_space, permission_info, action="update")
fluidinfo.call('PUT', permission_space, permission_info, action="delete")
fluidinfo.call('PUT', permission_space, permission_info, action="list")
fluidinfo.call('PUT', permission_space, permission_info, action="control")

### @end

