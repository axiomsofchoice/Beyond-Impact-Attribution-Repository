from biar.connection import Connection
from biar.collection import Collection
from biar.work import Work
import os

USERNAME = os.environ["FLUID_USERNAME"]
PASSWORD = os.environ["FLUID_PASSWORD"]

if not USERNAME:
    raise Exception("Please supply a fluid account username")

if not PASSWORD:
    raise Exception("Please supply a fluid account password")

conn = Connection.connect(USERNAME, PASSWORD)

print conn.username
print conn.user_info()
print conn.user_id()


mylist = Collection(conn, 'mylistx1')
assert mylist.exists_in_fluid()

work = Work.create(conn)
print "Created new work", work.object_id
mylist.add_work(work)
print mylist.list_works()

work.set_canonical_tag('title', "Abc")
print work.get_canonical_tag('title')
work.set_personal_tag('title', "Def")
print work.get_personal_tag('title')

