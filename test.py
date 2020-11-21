import re

list=['010036787714601021TK3C1RXC874HNY21722093010S001192','01003680250663032110000036327717230930102022271',
      '01003680250663032110000036327717230930102022271','0100365862845016211N7CEAEN8G3FHA61722053110CZSB20009-A',
      '010036846219605221V4T9T6VV0WF1172308311017201482']

for string in list:

    string=string.replace("","")

    date_x = re.findall('17[2]{1}[0-9]{1}[0-1]{1}[0-9]{1}[0-3]{1}[0-9]{1}', string)
    date_x=date_x[0]

    string = string.replace(date_x, "")
    date_x = '20' + date_x[2:4] + '-' + date_x[4:6] + '-' + date_x[6:8]

    gstin = re.findall('01[0-9]{14}', string)

    string = string.replace(gstin[0], '')
    gstin = gstin[0][2:]


    lot = re.findall('10[A-Za-z0-9]*[^(21)]', string)
    string = string.replace(lot[0], '')


    lot = str(lot[0]).replace('', "")
    lot = lot.replace('10', '')

    string=string.replace(lot,"")


    serial = re.findall(r'21[a-zA-Z0-9]*[^(10)]', string)

    if len(serial)==0:
        serial = re.findall(r'21[a-zA-Z0-9]*', string)


    serial=serial[0][2:]


    print([date_x,gstin,lot,serial])
