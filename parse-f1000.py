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

file_location = "/Users/ian/sandbox/f1000/small-f1000.xml"
xml = open(file_location, "r").read()
soup = BeautifulStoneSoup(xml)

articles = soup.findAll("article")
for article in articles[0:4]:
    doi =  article.doi.contents[0]
    title = article.title.contents[0]
    rating = article.rating.contents[0]
    pmid = doi2pmid(doi)
    print doi, pmid, rating




