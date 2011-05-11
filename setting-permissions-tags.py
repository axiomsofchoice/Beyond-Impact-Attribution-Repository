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

### @export "set-tag-permissions"
taglist=['author', 'keyword','series'
'is_video',
'is_blog_post',
'volume',
'year',
'name', 'pmid',
'short-name','grant_id',
'wonga']


def setPermOnTag(foo):
	
	permission_space = '/permissions/tags/biar/%s' % foo
	permission_info = {
	    'policy': 'closed',
	    'exceptions': ['birukou', 'ianmulvany', 'axiomsofchoice', 'svanderwaal', 'ananelson', 'biar']
	}
	fluidinfo.call('PUT', permission_space, permission_info, action="create")
	print headers
	print response
	fluidinfo.call('PUT', permission_space, permission_info, action="delete")
	print headers
	print response

map(setPermOnTag, taglist)

### @end

