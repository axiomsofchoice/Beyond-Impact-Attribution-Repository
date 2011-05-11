import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup
import urllib2

file_location = "/Users/ian/sandbox/Beyond-Impact-Attribution-Repository/UKPMC+_Grants.xml"
xml = open(file_location, "r").read()
soup = BeautifulStoneSoup(xml)

records = soup.findAll("record")
for grant in records[0:4]:
    grant_id = grant.grant.id.contents[0] 
    wonga = grant.amountawarded.contents[0] 
    title = grant.grant.title.contents[0] 
    print grant_id, wonga, title




