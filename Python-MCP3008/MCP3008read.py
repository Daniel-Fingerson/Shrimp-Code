def ReadChannel(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  volts= (data * 3.3) / float(1023)
  return volts


def Temp(data):
  temp = ((data * 330)/float(1023))-50
  temp = round(temp)
  return temp

