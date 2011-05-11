from biar.connection import Connection
from biar.collection import Collection
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


mylist = Collection(conn, 'mylist')
assert mylist.exists_in_fluid()



