import re

list=['010036787714601021TK3C1RXC874HNY21722093010S001192','01003680250663032110000036327717230930102022271',
      '01003680250663032110000036327717230930102022271','0100365862845016211N7CEAEN8G3FHA61722053110CZSB20009-A',
      '010036846219605221V4T9T6VV0WF1172308311017201482']



for string in list:

    bottle=[]

    string=string.replace("","")

    date_x = re.findall('17[2]{1}[0-9]{1}[0-1]{1}[0-9]{1}[0-3]{1}[0-9]{1}', string)
    date_x=date_x[0]


    string=string.split(date_x)
    date_x = '20' + date_x[2:4] + '-' + date_x[4:6] + '-' + date_x[6:8]
    bottle.append(date_x)


    after_gstin=[]

    for i in range(len(string)):

        gstin = re.findall('01[0-9]{14}', string[i])


        if len(gstin)>0:
            gstin = gstin[0][2:]
            bottle.append(gstin)
            temp=string[i].split(gstin[0])
            after_gstin.extend(temp)
        else:
            after_gstin.append(string[i])


    after_lot = []
    for j in range(len(after_gstin)):
        lot = re.findall('10[A-Za-z0-9]*', after_gstin[j])


        if len(lot)>0:
            lot=lot[0][2:]
            bottle.append(lot)
            temp = after_gstin[j].split(lot[0])
            after_lot.extend(temp)
        else:
            after_lot.append(after_gstin[j])


    after_serial = []
    #print(after_gstin)
    for j in range(len(after_lot)):
        serial = re.findall(r'21[a-zA-Z0-9]*', after_lot[j])


        if len(serial) > 0:
            serial=serial[0][2:]
            bottle.append(serial)
            temp = after_lot[j].split(serial[0])
            after_serial.extend(temp)
        else:
            after_serial.append(after_lot[j])










    print(bottle)
