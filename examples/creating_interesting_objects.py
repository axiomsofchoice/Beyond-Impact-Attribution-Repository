"""A set of example of works and the tags/metadata that might typically be provided in some basic use cases.
"""

from biar.connection import Connection
from biar.collection import Collection
from biar.work import Work
import os
import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup
import urllib2

def doi2pmid(doi):
    url = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?term=%s&email=ian.mulvany@gmail.com" % doi
    xml = urllib2.urlopen(url)
    for l in xml:
        if l.find("<Id>")!=-1:
            # <Id>16027735</Id>
            pmid = l.strip().replace("<Id>","").replace("</Id>", "")
            # strip of part after first _!
            return pmid
            
# connect to biar

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

# prepare f100 articles to create objects in biar

file_location = "/Users/ian/sandbox/f1000/small-f1000.xml"
xml = open(file_location, "r").read()
soup = BeautifulStoneSoup(xml)

articles = soup.findAll("article")
for article in articles:
    doi =  article.doi.contents[0]
    title = article.title.contents[0]
    rating = article.rating.contents[0]
    pmid = doi2pmid(doi)

    print doi, pmid, rating
    # Adding an example of a video, i.e. a canonical work
    articleWork = Work.create(conn)
    articleWork.set_canonical_tag('title', str(title))
    articleWork.set_canonical_tag('doi', str(doi))
    articleWork.set_canonical_tag('pmid', str(pmid))
    # now I want to add the f000 tag, which if I need to I can, I can do with a call to the fluidinfo API
    articleWork.set_personal_tag('f1000rating', str(rating))


# prepare grant info and add objects into biar

file_location = "/Users/ian/sandbox/Beyond-Impact-Attribution-Repository/UKPMC+_Grants.xml"
xml = open(file_location, "r").read()
soup = BeautifulStoneSoup(xml)

records = soup.findAll("record")
for grant in records:
    grant_id = grant.grant.id.contents[0] 
    wonga = grant.amountawarded.contents[0] 
    title = grant.grant.title.contents[0] 
    # Adding an example of a video, i.e. a canonical work
    grantWork = Work.create(conn)
    grantWork.set_canonical_tag('grant_id', str(grant_id))
    grantWork.set_canonical_tag('wonga', str(wonga))
    grantWork.set_canonical_tag('title', str(title))
    print grant_id, wonga, title

