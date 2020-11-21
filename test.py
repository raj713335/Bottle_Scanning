import re

list=['010036787714601021TK3C1RXC874HNY21722093010S001192','01003680250663032110000036327717230930102022271',
      '01003680250663032110000036327717230930102022271','0100365862845016211N7CEAEN8G3FHA61722053110CZSB20009-A',
      '010036846219605221V4T9T6VV0WF1172308311017201482']

for string in list:
    print(string)


    date_x = re.findall('17[2]{1}[0-9]{1}[0-1]{1}[0-9]{1}[0-3]{1}[0-9]{1}', string)
    date_x=date_x[0]
    print("date",date_x)
    string = string.replace(date_x, "")
    date_x = '20' + date_x[2:4] + '-' + date_x[4:6] + '-' + date_x[6:8]



    gstin = re.findall('01[0-9]{14}', string)

    print("gstin",gstin)



    string = string.replace(gstin[0], '')
    gstin = gstin[0][2:]

    print(string)

    serial = re.findall(r'21([a-zA-Z]|[0-9])*', string)
    print(serial)
    serial = serial[0][2:-1]

    lot = re.findall('10[A-Za-z0-9]*', string)
    string = string.replace(lot[0], '')


    lot = str(lot[0]).replace('', "")
    lot = lot.replace('10', '')




    print([date_x,gstin,lot,serial])
