import xml.etree.cElementTree as etree

xmlDoc = open('15717B-189380-200204171407.xml', 'r')
xmlDocData = xmlDoc.read()
xmlDocTree = etree.XML(xmlDocData)

for ingredient in xmlDocTree.iter('ingredient'):
    print (ingredient[0].text)


print("hhh")