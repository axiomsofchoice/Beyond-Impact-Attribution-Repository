import fluidinfo
import json
import os

USERNAME = os.environ["FLUID_USERNAME"]
PASSWORD = os.environ["FLUID_PASSWORD"]

if not USERNAME:
    raise Exception("Please supply a fluid account username")

if not PASSWORD:
    raise Exception("Please supply a fluid account password")

fluidinfo.login(USERNAME, PASSWORD)

# Create an object for an interesting book
r,payload = fluidinfo.call('POST', "/about/I Can Has Cheezburger?: A Lolcat Colleckshun")

cheezburgerId = payload['id']

"""
# Create a namespace to put some tags into
parent_namespace = '/namespaces/axiomsofchoice'
namespace_info = {
    'name': 'biar',
    'description': 'Beyond Impact Attribution Registry'
}
print "%s\n%s" % fluidinfo.call('POST', parent_namespace, namespace_info)

# Create a new tag for allowing me to like stuff
namespace = '/tags/axiomsofchoice/biar'
tag_info = {
   'name': 'likes', 'description': 'Things I like.', 'indexed': False
}
print "%s\n%s" % fluidinfo.call('POST', namespace, tag_info)

# Create a new tag for allowing me to like stuff
namespace = '/tags/axiomsofchoice/biar'
tag_info = {
   'name': 'listofcats', 'description': 'A list of cats.', 'indexed': False
}
print "%s\n%s" % fluidinfo.call('POST', namespace, tag_info)
"""

# Now tag up something I like :)
#print "%s\n%s" % fluidinfo.call('PUT', '/about/%s/axiomsofchoice/biar/likes' % cheezburgerId)

# put a list (first example is an opaque JSON version and the second is the primitive set of string)
#print "%s\n%s" % fluidinfo.call('PUT', '/about/%s/axiomsofchoice/biar/listofcats' % cheezburgerId, json.dumps([1,2]), mime="application/json")
print "%s\n%s" % fluidinfo.call('PUT', '/about/%s/axiomsofchoice/biar/listofcats' % cheezburgerId, ['1','2'])

# Get an example of a list of things
print "%s\n%s" % fluidinfo.call('GET', '/objects/331b8880-b5b6-4f26-8a3a-2e33a90e5c5b/oreilly.com/authors/works', showAbout=True)
