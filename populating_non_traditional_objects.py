import biar

foo = Work()

foo.SetCanonicalTag('url','http://www.youtube.com/watch?v=AaabJdRI3pE')
foo.SetCanonicalTag('title', 'FET11 Instant Communities tool')
foo.SetCanonicalTag('author', ['Marcos Baez', 'Lyubov Kolosovskaya'])
foo.SetPersonalTag('publisher','mbaezpy')
foo.SetCanonicalTag('is_video', 1)

foo.SetCanonicalTag('url','http://www.fet11.eu/instantcommunities#/panel/332')
foo.SetCanonicalTag('title', 'Science Caf� with Robert Madelin: What more should be done to empower Young Scientists in Europe?')

foo.SetCanonicalTag('url','http://beyond-impact.org/?p=35')
foo.SetCanonicalTag('title', 'The personal impact dashboard')
foo.SetCanonicalTag('author', 'Cameron Neylon')
foo.SetPersonalTag('keyword', ['Funders', 'News', 'Researchers'])
foo.SetCanonicalTag('is_blog', 1)

foo.SetCanonicalTag('doi', '10.1007/978-3-642-19513-6') 
foo.SetCanonicalTag('series', 'LECTURE NOTES OF THE INSTITUTE FOR COMPUTER SCIENCES, SOCIAL INFORMATICS AND TELECOMMUNICATIONS ENGINEERING')
foo.SetCanonicalTag('volume', 53)
foo.SetCanonicalTag('year', 2011)
foo.SetCanonicalTag('title',  'Digital Forensics and Cyber Crime. Second International ICST Conference, ICDF2C 2010, Abu Dhabi, United Arab Emirates, October 4-6, 2010, Revised Selected Papers')
foo.SetCanonicalTag('author', 'Ibrahim Baggili')

lic = List()
lic.addWork('title', 'Digital Forensics and Cyber Crime. Second International ICST Conference, ICDF2C 2010, Abu Dhabi, United Arab Emirates, October 4-6, 2010, Revised Selected Papers')
foo.SetCanonicalTag('series', 'LECTURE NOTES OF THE INSTITUTE FOR COMPUTER SCIENCES, SOCIAL INFORMATICS AND TELECOMMUNICATIONS ENGINEERING')

foo.SetPersonalTag('series', 'LNICST')

