import serial
import serial.tools.list_ports

# Port initialization
serialInst = serial.Serial()

serialInst = serial.Serial("/dev/ttyS0", baudrate = 9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)


#Read Serial Port
i=0

while i==0:
    
    if serialInst.in_waiting:    
        packet = serialInst.readline()
        #print(str((out*100)/samples)+'%')
        if(packet.decode() != ''):
         print(packet.decode()) 