import re

a2,b2,c2,d2,e2=str(0),str(0),str(0),str(0),str(0)

with open('DATA/Scanning/data.txt', 'r') as fh:
    all_lines = fh.readlines()
    for each in all_lines:
        string = str(each)

if a2 == str(0):
    date_x = re.findall('17[2]{1}[0-9]{5}', string)
    string=string.replace(date_x[0],"")
    print(date_x,0)
    print(string)
    try:
        date_x = date_x[0]
    except:
        date_x = ''
    date_x = '20' + date_x[2:4] + '-' + date_x[4:6] + '-' + date_x[6:8]
else:
    date_x = a2

if b2 == str(0):

    lot = re.findall(r'10[A-Za-z]{2}[0-9]*[]*', string)
    try:
        lot = str(lot[0]).replace('', "")
        lot = lot.replace('10', '')
    except:
        lot = ''
else:
    lot = b2

if c2 == str(0):
    gstin = re.findall('01[0-9]{14}', string)
    try:
        gstin = gstin[0][2:]
    except:
        gstin = ''
else:
    gstin = c2

if d2 == str(0):
    total = ""
else:
    total = d2

if e2 == str(0):
    serial = re.findall(r'21[0-9]*', string)
    try:
        serial = serial[0][2:-1]
    except:
        serial = ''
else:
    serial = e2



print(date_x)
print(lot)
print(gstin)
print(serial)
