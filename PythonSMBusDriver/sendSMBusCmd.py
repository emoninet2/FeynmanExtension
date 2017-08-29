# to use the command type :
# $python sendSMBusCmd.py <your command in qoute>



import sys
import smbus
def main():
	#print(sys.argv[1])
	bus = smbus.SMBus(1)
	FyenmanExtDevAddr = 0x08

	if(sys.argv[1] == "-s"):
		data = []
		for d in sys.argv[2]:
			data.append(ord(d))
			#print hex(ord(d))
		data.append(10)
		#print(data)
	
		for i in data:
			bus.write_byte(FyenmanExtDevAddr, i)
	elif(sys.argv[1] == "-r");
		print("reset");
	else:
		print("unknown command")

if __name__ == "__main__":
    main()
