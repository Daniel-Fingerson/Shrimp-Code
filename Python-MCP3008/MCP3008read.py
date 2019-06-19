mport spidev

spi=spidev.SpiDev()
spi.open(0,0)

def read():
	buf0=[0x01,0x00,0x00]
	spi.xfer2(buf0)
	print(buf0[0],buf0[1],buf0[2])
	print("This is Channels 0-1")

