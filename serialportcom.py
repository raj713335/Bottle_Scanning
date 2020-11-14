

def Read():

    import time
    import serial, string
    import RPi.GPIO as IO



    Bottle=[]
    z1serial=serial.Serial('/dev/ttyUSB0',115200)
    reading=''
    while True:
        size = z1serial.inWaiting()
        if size:
            data = z1serial.read(size)
            data = data.decode()
            print(data)
            if '\r' in data:
                break
        else:
            print('no data')
        time.sleep(1)
    decode=data
    #print decode
    if  decode[0:3] == '(01':
        GTIN=gtin=decode[3:17]
        #print 'GTIN:',gtin
        agdecode=decode[17:len(decode)]
        if agdecode[0:2]=='21':
            SN=agdecode[2:agdecode.index('\x1d')]
            #print 'SN:',SN
            asdecode=agdecode[len(SN)+3:len(agdecode)]

            if asdecode[0:2]=='17':
                EXP=asdecode[2:8]
                #print 'EXP:',EXP
                aedecode=asdecode[8:len(asdecode)]
                LOT= aedecode[2:aedecode.index('\r')]
                #print 'LOT:',LOT
                Bottle= [GTIN,EXP,LOT]

    return (Bottle)


data = Read()
print('Got Data as:', data)