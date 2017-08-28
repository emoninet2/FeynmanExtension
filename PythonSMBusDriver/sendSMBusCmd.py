# to use the command type :
# $python sendSMBusCmd.py <your command in qoute>



import sys
import smbus
def main():
	#print(sys.argv[1])
	bus = smbus.SMBus(1)
	FyenmanExtDevAddr = 0x08


	data = []
	for d in sys.argv[1]:
		data.append(ord(d))
		#print hex(ord(d))
	data.append(10)
	#print(data)

	for i in data:
		bus.write_byte(FyenmanExtDevAddr, i)



if __name__ == "__main__":
    main()
