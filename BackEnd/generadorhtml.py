import lxml.etree as ET



dom = ET.parse("floradesdemongodb.xml")

xslt = ET.parse("flora.xsl")

transform = ET.XSLT(xslt)

newdom = transform(dom)

print(newdom)

#output = ET.tostring(newdom)



f = open("flora.html", "w")

f.write(str(newdom))

f.close()