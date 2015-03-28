#from xml.dom import minidom                                          
from lxml import etree
from StringIO import StringIO

dtd = etree.DTD(StringIO("""<!ELEMENT p2pse (getHosts?, getHostsResponse?, searchFile?, searchFileResponse?, getFiles?, getFilesResponse?)>
  <!ELEMENT getHosts EMPTY>
  <!ELEMENT getHostsResponse (host*)>
     <!ELEMENT host (ip?,port?)>
        <!ELEMENT ip (#PCDATA)> 
        <!ELEMENT port (#PCDATA)> 
  <!ELEMENT searchFile (keywords?)>
     <!ELEMENT keywords (#PCDATA)>
  <!ELEMENT searchFileResponse (file*)>
     <!ELEMENT file (fileName?, fileSize?)>
        <!ELEMENT fileName (#PCDATA)> 
        <!ELEMENT fileSize (#PCDATA)> 
  <!ELEMENT getFiles (fileName*)>    
  <!ELEMENT getFilesResponse (fileData*)>
     <!ELEMENT fileData (fileName?, data?)> 
        <!ELEMENT data (#PCDATA)> 
        <!ATTLIST data encode CDATA #REQUIRED>

 """))

root = etree.XML("""<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE p2pse SYSTEM "p2pse.dtd">
	<p2pse>
			<getHostsResponse>
		<host>
			<ip>10.67.5.1</ip>
			<port>3121</port>
		</host>
		<host>
			<ip>10.67.5.7</ip>
			<port>1024</port>
		</host>
	  </getHostsResponse>
	</p2pse>""")

print(dtd.validate(root))


'''
xmlschema_doc = etree.parse('hosts.dtd')
xml_doc = etree.parse('hostlist.xml')
xmlschema = etree.XMLSchema(xmlschema_doc)

if xmlschema.validate(xml_doc):
   print 'Valid xml'
else:
   print 'Invalid xml'
'''

#root = etree.XML("<foo>bar</foo>")
#print(dtd.validate(root))
