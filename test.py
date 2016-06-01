import serial
import time
def genCommandString(axis,direction,steps,delay):
	return axis+"%"+str(direction)+"%"+str(steps)+"%"+str(delay)+"%"
	print("Operation ETA: "+str(steps*delay/1000)+" seconds")
def moveMillimetres(axis,direction,distance):
	stepsPerMillimetre=20 #TODO: get distance for this
	delay=100
	print("Operation ETA:"+str(stepsPerMillimetre*distance*delay*2/1000)+"")
	steps=stepsPerMillimetre*distance
	return genCommandString(axis,direction,steps,delay)
	
print(genCommandString("x",1,100,100))
ser = serial.Serial("COM6")  # open first serial port
time.sleep(2)
i=moveMillimetres("x",1,1)
ser.write(bytes(i, 'utf-8'))      # write a string
print("cancer")
ser.close()             # close port
