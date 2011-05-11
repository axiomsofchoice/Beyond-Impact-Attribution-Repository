### @export "imports"
import sys
import getpass
import fluidinfo
import json
import os
import urllib
from biar.connection import Connection

LIST_TAG = 'biar/collection'

def printListItems(list_name):
    LIST_TAG = 'biar/collection'
    headers, response = fluidinfo.call('GET', '/objects', query='%s matches "%s"' % (LIST_TAG, list_name))
    print response

    return 


def printAllLists():
    headers, response = fluidinfo.call('GET', '/objects', query='has %s' % LIST_TAG)

    for obj_id in response['ids']:
        object_tag_path = "/objects/%s/%s" % (obj_id, LIST_TAG)
        details_h, details_response = fluidinfo.call('GET', object_tag_path)
        print details_response
    return 

def logIn():
    """Provides a session where a user logs in and 
    """
    
    print
    print "Welcome to Beyond Impact Attribute Repository (BIAR)."
    print
    username = raw_input("Please enter your fluidinfo username : ")
    password = getpass.getpass("Enter your fuidinfo password: ")

    if not username:
        raise Exception("Please supply a fluid account username")

    if not password:
        raise Exception("Please supply a fluid account password")
    conn = Connection.connect(username, password)

    print 
    print "Welcome",conn.user_name()
    print
        
    return

def getAndRunCommand():
    full_cmd = raw_input("Choose command (lists, elements <listid>, exit): ").split()
    cmd = full_cmd[0]
    print

    if cmd == "lists":
	    printAllLists();
    elif cmd == "elements":
	    printListItems(full_cmd[1]);
    elif cmd == "exit":
        print "Thanks for using BIAR. Now exiting..."
        sys.exit();
    else:
        print "Command",cmd,"not recognised."
    return
	
def main():
    try:
        logIn()
        while(True):
            getAndRunCommand()
            print

    except Exception as e:
        print(str(e))
        raise e

if __name__ == "__main__":
    main()
