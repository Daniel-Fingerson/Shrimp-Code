import spidev
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
buf=[0x00,0x01,0x02,0x03]

def select(channel):
    spi=spidev.SpiDev()
    spi.open(0,0)
    if channel==0:
        spi.xfer2(buf[0])
        print("Device 0 selected")
    if channel==1:
        spi.xfer2(buf[1])
        print("Device 1 selected")

def read(channel):
    buf0=[ 0x01, 0x00, 0x00]
    spi=spidev.SpiDev()
    spi.open(0,1)
    spi.xfer2(buf0)
    print(buf0)
