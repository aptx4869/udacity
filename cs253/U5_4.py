import urllib2
#p = urllib2.urlopen("http://www.example.com")
#print p.headers['server']
from xml.dom import minidom
#x = minidom.parseString("<mytag><c1>c1</c1>a</mytag>")
#print x.toprettyxml()
#p = urllib2.urlopen("http://www.nytimes.com/services/xml/rss/nyt/GlobalHome.xml")
#y = minidom.parseString(p.read())
#print dir(y)
#z = y.getElementsByTagName('item')

#print dir(z)
#print z
#print len(z)
import json
j = '{"one": 1, "numbers": [1,2,3,4,5]}'
d = json.loads(j)
print dir(d)
print dir(d.tool)
print d['numbers']
