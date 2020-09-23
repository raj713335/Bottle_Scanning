from datetime import datetime
from xml.dom import minidom
from xml.dom.minidom import getDOMImplementation

root = minidom.Document()
root.standalone = 'No'

iso_date = datetime.now().astimezone().isoformat()
offset = iso_date[-6:]
expire_date = "2021-08-31"
bulk_lot_number = "15717B"
repackage_lot_number = "189380"
strings = ['0100351991877905211000002131\x1d10DT1902039A\x1d17210131', '010036050500950321896508\x1d1722113010PV5665', '0100351991877905211000002131\x1d10DT1902039A\x1d17210131', '0100369238149050211000020346\x1d1721103110AM191242B', '01003078159880122191409307188300\x1d1721083110FX000563', '0100351991877905211000002131\x1d10DT1902039A\x1d17210131']



list_data=''

for each in strings:
    list_data+=str('<epcis:epc>')+each+str('</epcis:epc>')

string = f'''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<epcis:EPCISDocument xmlns:epcis="urn:epcglobal:epcis:xsd:1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" creationDate="{iso_date}" schemaVersion="1">
<epcis:EPCISBody>
<epcis:EventList>
<epcis:ObjectEvent>
<epcis:eventTime>{iso_date}</epcis:eventTime>
<epcis:eventTimeZoneOffset>{offset}</epcis:eventTimeZoneOffset>
<epcis:epcList>'''+str(list_data)+'''
</epcis:epcList>
<epcis:action>ADD</epcis:action>
<epcis:bizStep>urn:epcglobal:cbv:bizstep:commissioning</epcis:bizStep>
<epcis:disposition>urn:epcglobal:cbv:disp:active</epcis:disposition>
<epcis:readPoint>
<epcis:id>urn:systechcitadel.com:device:sgln:101</epcis:id>
</epcis:readPoint>
<epcis:bizLocation>
<epcis:id>urn:epc:id:sgln:08662190003.0.0</epcis:id>
</epcis:bizLocation>
<epcis:extension><!--@Verify By ykhatri-->
<epcis:field name="Lot Number (Bulk)" value="{bulk_lot_number}"/>
<epcis:field name="Expiration Date" value="{expire_date}"/>
<epcis:field name="Lot Number (Repackaged)" value="{repackage_lot_number}"/>
</epcis:extension>
</epcis:ObjectEvent>
</epcis:EventList>
</epcis:EPCISBody>
</epcis:EPCISDocument>
'''

dom = minidom.parseString(string)

xml_str = dom.toprettyxml(indent="  ", newl='', encoding='UTF-8')
timestamp = int(datetime.now().timestamp())
save_path_file = f"{bulk_lot_number}-{repackage_lot_number}-{timestamp}.xml"

with open(save_path_file, "w") as f:
    f.write(xml_str.decode())
