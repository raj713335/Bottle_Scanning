

def Read():

	import time
	import serial, string
	import RPi.GPIO as IO



	Bottle=[]
	ser=serial.Serial('/dev/ttyUSB0',115200)
	ser.flushInput()
	reading=''
	IO.setmode(IO.BOARD)
	IO.setwarnings(False)
	IO.setup(23,IO.OUT)
	IO.output(23,False)
	while True:
		try:
			r=ser.read()
			reading=reading+r
			if ')' in reading:
				break
		except:
			print("KeyError")
			break
	decode=(reading[0:len(reading)])
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
				LOT= aedecode[2:aedecode.index(')')]
				#print 'LOT:',LOT
				IO.output(23,True)
				time.sleep(1)
				IO.output(23,False)
				Bottle= [GTIN,EXP,LOT]
	return (Bottle)
