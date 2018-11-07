#written entirely by Daniel Fingerson
#this is the first steps toward supplying real data from our new 24 bit analalog to digital converter (we were previously using an MCP3008 ADC)
#currently only reads the differential voltages between the first and second sensor channels (0+ and 1-)
import spidev
spi=spidev.SpiDev()
spi.open(0,0)
def read():
    buf0=[0xA0,0x00,0x00,0x00]
    spi.xfer2(buf0)
    #print('{0:03d} {1:03d} {2:03d} {3:03d}').format(buf0[0],buf0[1],buf0[2],buf0[3])
    ADC_reading=buf0[0]+buf0[1]+buf0[2]+buf0[3]
    #24 bit ADC resolution= 2^24=16,777,216
    voltage=(16777216/5)/ADC_reading
    return voltage
