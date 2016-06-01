import serial
ser = serial.Serial("COM6")  # open first serial port
i="1100t100t"
ser.write(bytes(i, 'utf-8'))      # write a string
print("cancer")
print(ser.read())
ser.close()             # close port