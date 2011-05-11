"""A set of example of works and the tags/metadata that might typically be provided in some basic use cases.
"""

from biar.work import Work

# Adding an example of a video, i.e. a canonical work
videoWork = Work()
videoWork.SetCanonicalTag('url','http://www.youtube.com/watch?v=AaabJdRI3pE')
videoWork.SetCanonicalTag('title', 'FET11 Instant Communities tool')
videoWork.SetCanonicalTag('author', ['Marcos Baez', 'Lyubov Kolosovskaya'])
videoWork.SetPersonalTag('publisher','mbaezpy')
videoWork.SetCanonicalTag('is_video', 1)

# Adding an example of a webpage
webpageWork = Work()
webpageWork.SetCanonicalTag('url','http://www.fet11.eu/instantcommunities#/panel/332')
webpageWork.SetCanonicalTag('title', 'Science Café with Robert Madelin: What more should be done to empower Young Scientists in Europe?')

# An example of a blog post
blogpostWork = Work()
blogpostWork.SetCanonicalTag('url','http://beyond-impact.org/?p=35')
blogpostWork.SetCanonicalTag('title', 'The personal impact dashboard')
blogpostWork.SetCanonicalTag('author', 'Cameron Neylon')
blogpostWork.SetPersonalTag('keyword', ['Funders', 'News', 'Researchers'])
blogpostWork.SetCanonicalTag('is_blog_post', 1)

# An example of a book
book1Work = Work()
book1Work.SetCanonicalTag('doi', '10.1007/978-3-642-19513-6') 
book1Work.SetCanonicalTag('series', 'LECTURE NOTES OF THE INSTITUTE FOR COMPUTER SCIENCES, SOCIAL INFORMATICS AND TELECOMMUNICATIONS ENGINEERING')
book1Work.SetCanonicalTag('volume', 53)
book1Work.SetCanonicalTag('year', 2011)
book1Work.SetCanonicalTag('title',  'Digital Forensics and Cyber Crime. Second International ICST Conference, ICDF2C 2010, Abu Dhabi, United Arab Emirates, October 4-6, 2010, Revised Selected Papers')
foo4.SetCanonicalTag('author', 'Ibrahim Baggili')

# An other example of a book
book2Work = Work()
book2Work.SetCanonicalTag('doi', '10.1007/978-3-642-19385-9') 
book2Work.SetCanonicalTag('series', 'LECTURE NOTES OF THE INSTITUTE FOR COMPUTER SCIENCES, SOCIAL INFORMATICS AND TELECOMMUNICATIONS ENGINEERING')
book2Work.SetCanonicalTag('volume', 59)
book2Work.SetCanonicalTag('year', 2011)
book2Work.SetCanonicalTag('title',  'Human-Robot Personal Relationships Third International Conference, HRPR 2010, Leiden, The Netherlands, June 23-24, 2010, Revised Selected Papers')
book2Work.SetCanonicalTag('author', ['Maarten H. Lamers', 'Fons J. Verbeek'])

# A list of books in the same series
lic = List()
lic.SetCanonicalTag('name', 'LECTURE NOTES OF THE INSTITUTE FOR COMPUTER SCIENCES, SOCIAL INFORMATICS AND TELECOMMUNICATIONS ENGINEERING')
lic.SetCanonicalTag('short-name', 'LNICST');
lic.addWork(book1Work);
lic.addWork(book2Work);
