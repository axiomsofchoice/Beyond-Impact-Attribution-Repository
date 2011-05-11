import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup
import json
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

def pmid2grant(pmid):
    # generate a query session key
    url = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/epost.fcgi?db=pubmed&id=%s" % pmid
    pxml = urllib2.urlopen(url).read()
    psoup =  BeautifulStoneSoup(pxml)
    query_key = psoup.querykey.contents[0]
    webenv = psoup.webenv.contents[0]
    # query for the grant info
    url = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&query_key=%s&WebEnv=%s&retmode=xml" % (query_key, webenv)
    gxml = urllib2.urlopen(url).read()
    soup = BeautifulStoneSoup(gxml)
    try:
        grant = soup.GrantID.contents[0]
        print grant 
        return grant
    except:
        return "no grant"
articles = soup.findAll('article')
for article in articles:
    doi =  article.doi.contents[0]
    pmid = convert(doi)
    grant = pmid2grant(pmid)
    print doi, pmid, grant
    #print article.rating.contents[0]
    #print article.title.contents[0]
### lookup mendleey info my doi


### create fluidinfo objects 



