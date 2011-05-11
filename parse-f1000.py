

from BeautifulSoup import BeautifulStoneSoup
import urllib2
file_location = "/Users/ian/sandbox/f1000/small-f1000.xml"
xml = open(file_location, "r").read()
soup = BeautifulStoneSoup(xml)

### convert doi to pmid

def convert(doi):
    url = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?term=%s&email=ian.mulvany@gmail.com" % doi
    xml = urllib2.urlopen(url)
    for l in xml:
        if l.find("<Id>")!=-1:
            # <Id>16027735</Id>
            pmid = l.strip().replace("<Id>","").replace("</Id>", "")
            # strip of part after first _!
            return pmid



articles = soup.findAll('article')
for article in articles:
    doi =  article.doi.contents[0]
    pmid = convert(doi)
    print doi, pmid
    #print article.rating.contents[0]
    #print article.title.contents[0]
### lookup mendleey info my doi


### create fluidinfo objects 



