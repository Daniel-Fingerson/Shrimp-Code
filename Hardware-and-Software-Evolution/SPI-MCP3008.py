import spidev
spi=spidev.SpiDev()
spi.open(0,1)
def select(channel):
//the python version of eric’s c code for spi select
    if channel==0:
        buf='0x00'
        spi.transfer(buf,1)
        print("Device 0 has been selected")
    if channel==1:
        buf='0x01'
        spi.transfer(buf,1)
        print("Device 1 has been selected")
    if channel==2:
        buf='0x02'
        spi.transfer(buf,1)
        print("Device 2 has been selected")
    if channel==3:
        buf='0x03'
        spi.transfer(buf,1)
        print("Device 3 has been selected")
    if channel==4:
        buf='0x04'
        spi.transfer(buf,1)
        print("Device 4 has been selected")
    if channel==5:
        buf='0x05'
        spi.transfer(buf,1)
        print("Device 5 has been selected")
    if channel==6:
        buf='0x06'
        spi.transfer(buf,1)
        print("Device 6 has been selected")
    if channel==7:
        buf='0x07'
        spi.transfer(buf,1)
        print("Device 7 has been selected")
    if channel==8:
        buf='0x08'
        spi.transfer(buf,1)
        print("Device 8 has been selected")
    if channel==9:
        buf='0x09'
        spi.transfer(buf,1)
        print("Device 9 has been selected")
    if channel==A:
        buf='0x0A'
        spi.transfer(buf,1)
        print("Device 10 has been selected")
    if channel==B:
        buf='0x0B'
        spi.transfer(buf,1)
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
select(0)

def ReadChannel(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data
 
# Function to convert data to voltage level,
# rounded to specified number of decimal places.
def ConvertVolts(data,places):
  volts = (data * 3.3) / float(1023)
  volts = round(volts,places)
  return volts
//python implementation of eric’s c code of the “read” fucntion
def read():
    buf0=['0x01', '0x00', '0x00']
    spi.transfer(buf0,len(buf0))
    print('{0:03d} {1:03d} {2:03d}').format(buf0[0],buf0[1],buf0[2])
