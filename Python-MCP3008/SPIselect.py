#written by Daniel Fingerson
import spidev
spi=spidev.SpiDev()
spi.open(0,1)
def select(channel):
//the python version of eric’s c code for spi select
//include: set clock speed to 65536, and set cs0 to low
    if channel==0:
        buf=[0x00]
        spi.xfer2(buf)
        print("Device 0 has been selected")
    if channel==1:
        buf=[0x01]
        spi.xfer2(buf)
        print("Device 1 has been selected")
    if channel==2:
        buf=[0x02]
        spi.xfer2(buf)
        print("Device 2 has been selected")
    if channel==3:
        buf=[0x03]
        spi.xfer2(buf)
        print("Device 3 has been selected")
    if channel==4:
        buf=[0x04]
        spi.xfer2(buf)
        print("Device 4 has been selected")
    if channel==5:
        buf=[0x05]
        spi.xfer2(buf)
        print("Device 5 has been selected")
    if channel==6:
        buf=[0x06]
        spi.xfer2(buf)
        print("Device 6 has been selected")
    if channel==7:
        buf=[0x07]
        spi.xfer2(buf)
        print("Device 7 has been selected")
    if channel==8:
        buf=[0x08]
        spi.xfer2(buf)
        print("Device 8 has been selected")
    if channel==9:
        buf=[0x09]
        spi.xfer2(buf)
        print("Device 9 has been selected")
    if channel==A:
        buf='0x0A'
        spi.xfer2(buf)
        print("Device 10 has been selected")
    if channel==B:
        buf=[0x0B]
        spi.xfer2(buf)
        print("Device 11 has been selected")
    if channel==C:
        buf='0x0C'
        spi.transfer(buf,1)
        print("Device 12 has been selected")
    if channel==D:
        buf='0x0D'
        spi.transfer(buf,1)
        print("Device 13 has been selected")
    if channel==E:
        buf='0x0E'
        spi.transfer(buf,1)
        print("Device 14 has been selected")
    if channel==F:
        buf='0x0F'
        spi.transfer(buf,1)
        print("Device 15 has been selected")
