import biar

# Adding an example of a video, i.e. a canonical work
foo1 = Work()
foo1.SetCanonicalTag('url','http://www.youtube.com/watch?v=AaabJdRI3pE')
foo1.SetCanonicalTag('title', 'FET11 Instant Communities tool')
foo1.SetCanonicalTag('author', ['Marcos Baez', 'Lyubov Kolosovskaya'])
foo1.SetPersonalTag('publisher','mbaezpy')
foo1.SetCanonicalTag('is_video', 1)

# Adding an example of a webpage,
foo2 = Work()
foo2.SetCanonicalTag('url','http://www.fet11.eu/instantcommunities#/panel/332')
foo2.SetCanonicalTag('title', 'Science Café with Robert Madelin: What more should be done to empower Young Scientists in Europe?')

foo.SetCanonicalTag('url','http://beyond-impact.org/?p=35')
foo.SetCanonicalTag('title', 'The personal impact dashboard')
foo.SetCanonicalTag('author', 'Cameron Neylon')
foo.SetPersonalTag('keyword', ['Funders', 'News', 'Researchers'])
foo.SetCanonicalTag('is_blog', 1)

foo4 = Work()
foo.SetCanonicalTag('doi', '10.1007/978-3-642-19513-6') 
foo.SetCanonicalTag('series', 'LECTURE NOTES OF THE INSTITUTE FOR COMPUTER SCIENCES, SOCIAL INFORMATICS AND TELECOMMUNICATIONS ENGINEERING')
foo.SetCanonicalTag('volume', 53)
foo.SetCanonicalTag('year', 2011)
foo.SetCanonicalTag('title',  'Digital Forensics and Cyber Crime. Second International ICST Conference, ICDF2C 2010, Abu Dhabi, United Arab Emirates, October 4-6, 2010, Revised Selected Papers')
foo.SetCanonicalTag('author', 'Ibrahim Baggili')

foo5 = Work()
foo.SetCanonicalTag('doi', '10.1007/978-3-642-19385-9') 
foo.SetCanonicalTag('series', 'LECTURE NOTES OF THE INSTITUTE FOR COMPUTER SCIENCES, SOCIAL INFORMATICS AND TELECOMMUNICATIONS ENGINEERING')
foo.SetCanonicalTag('volume', 59)
foo.SetCanonicalTag('year', 2011)
foo.SetCanonicalTag('title',  'Human-Robot Personal Relationships Third International Conference, HRPR 2010, Leiden, The Netherlands, June 23-24, 2010, Revised Selected Papers')
foo.SetCanonicalTag('author', ['Maarten H. Lamers', 'Fons J. Verbeek'])

lic = List()
lic.SetCanonicalTag('name', 'LECTURE NOTES OF THE INSTITUTE FOR COMPUTER SCIENCES, SOCIAL INFORMATICS AND TELECOMMUNICATIONS ENGINEERING')
lic.SetCanonicalTag('short-name', 'LNICST');
lic.addWork(foo4);
lic.addWork(foo5);
