
import spidev
spi=spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1350000

def read():
    buf0=[0xA0,0x00,0x00,0x00]
    spi.xfer2(buf0)
    print(buf0)
    
