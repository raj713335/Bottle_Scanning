import re
phoneNumRegex = re.compile(r'10[0-9]{14}')
mo = phoneNumRegex.search('010035199187790521100000213110DT1902039A17210131')
print('Phone number found: ' + mo.group())


"""

String has 4 thing all have identifier

Sample String:
010035199187790521100000213110DT1902039A17210131


Extracted data:
GTIN: 00351991877905
SERIAL: 1000002131
LOT: DT1902039A
EXP: 210131

Bifurcation:
01 means GTIN IT WILL ALWAYS 14 DIGIT

21 means serial number end with fnc(specific hax key)

10 mean LOT end with fnc

17 means exp which in all ways YYMMDD FORMAT

"""