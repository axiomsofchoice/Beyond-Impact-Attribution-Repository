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

# statistical methods in cosmology
headers, response = fluidinfo.call('POST', "/about/arXiv:0906.0664v3")

# create a tag that I can use later
headers, response = fluidinfo.call('PUT', '/about/arXiv:0906.0664v3/ianmulvany/set', "testing set", mime="text")

# now we tag the object
headers, response = fluidinfo.call('PUT', '/about/arXiv:0906.0664v3/ianmulvany/set', "testing set", mime="text")

print headers
print response


