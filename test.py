if a1 == str(0):
    date_x = re.findall('17[2]{1}[0-9]{1}[0-1]{1}[0-9]{1}[0-3]{1}[0-9]{1}', string)
    string = string.replace(date_x[0], "")
    try:
        date_x = date_x[0]
    except:
        date_x = ''
    date_x = '20' + date_x[2:4] + '-' + date_x[4:6] + '-' + date_x[6:8]
else:
    date_x = a1

if c1 == str(0):
    gstin = re.findall('01[0-9]{14}', string)
    string = string.replace(gstin[0], '')
    try:
        gstin = gstin[0][2:]
    except:
        gstin = ''
else:
    gstin = c1

if b1 == str(0):
    lot = re.findall('10[A-Za-z]{2}[0-9]*', string)
    string = string.replace(lot[0], '')
    try:
        lot = str(lot[0]).replace('', "")
        lot = lot.replace('10', '')
    except:
        lot = ''
else:
    lot = b1

if d1 == str(0):
    total = ""
else:
    total = d1

if f1 == str(0):
    total_bottles = ""
else:
    total_bottles = f1

if e1 == str(0):
    serial = re.findall(r'21[0-9]*', string)
    try:
        serial = serial[0][2:-1]
    except:
        serial = ''
else:
    serial = e1
