#extremely basic code for LC2418 meant for the purposes of testing:
#will add more functionality once it can succesfully read at least one single ended channel
#I have left so many comments since at the moment I cannot enter Byrne since it is Sunday, so I have no way of testing the code/debugging my problems at the bottom

#if it doesnt return expected voltage once the conversion is figured out, it is probably due to (in order of likelihood:)
#1. incorrect clock speed
#2. incorrect voltage conversion formula
#3. wrong read command
#4. wrong spi.open channel
#5. genearl mistake in code

import spidev
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
def read(channel): #only have 3 channels for the purposes of testing; normally has 15/ 8 differential
    #eventually will have read and display all channels automatically rather then manually
    spi=spidev.SpiDev()
    spi.open(0,0)
    spi.max_speed_hz=10000000 #clock speed=10 MHz
    command=[[0,0,0,0xB000],[0,0,0,0xB800],[0,0,0,0xB100]]
    if channel==0:
        spi.xfer2(command[0])
    if channel==1:
        spi.xfer2(command[1])
    if channel==2:
        spi.xfer2(command[2])
    #convert adc value to a voltage
    adc_code=command[channel] #adc value

    #from this point on it is hard for me to determine how to convert to a voltage:
    #I commented the rest out since it may be a broken conversion formula
    #datasheet code converts via the following formula, there is probably a better method:
    

    #adc_code=adc_code>>6 #Don't care about the first 6 bytes of the 32 bit data stream
    #adc_code -= 8388608 #2^23:the only bits we care about
    #adc_voltage=((float)adc_code+LTC2418_offset_code)*(LTC2418_lsb)

    #the problem is that I do not know what offset code and lsb are
    #the lsb may be as simple as finding the first/last item of the adc_code
    #I do not know however which variable (via adc_code? after its bit shifted? further conversion needed?) to grab it from/ if I can do that via an array or if I would have to bit shift
    
    #the datasheets method of finding these values is (written in C):

    '''

    void LTC2418_cal_voltage(int32_t zero_code, int32_t fs_code, float zero_voltage, float fs_voltage, float *LTC2418_lsb , int32_t *LTC2418_offset_code)
// Calibrate the lsb
{
  zero_code = zero_code >> 6;   //! 1) Bit-shift zero code to the right 6 bits
  zero_code -= 8388608;         //! 2) Convert zero code from offset binary to binary
  fs_code = fs_code >> 6;       //! 3) Bit-shift full scale code to the right 6 bits
  fs_code -= 8388608;           //! 4) Convert full scale code from offset binary to binary
  
  float temp_offset;
  *LTC2418_lsb = (fs_voltage-zero_voltage)/((float)(fs_code - zero_code));                              //! 5) Calculate the LSB
  
  temp_offset = (zero_voltage/ *LTC2418_lsb) - zero_code;                                               //! 6) Calculate Unipolar offset
  temp_offset = (temp_offset > (floor(temp_offset) + 0.5)) ? ceil(temp_offset) : floor(temp_offset);    //! 7) Round
  *LTC2418_offset_code = (int32_t)temp_offset;
  '''

  #Once again, I do not know what the paramaters are even referring to let alone their values
  #I will ask Eric/Steve if they know what it is referring to
  #and if they know at which point in code that I would able to do a simple ADC resolution voltage conversion, or just in genearl how to do a conversion from what I have so fa
    #I believe that, following defining the adc_code, this may be the correct conversion opeartion:

    #adc_code=adc_code>>6 #Don't care about the first 6 bytes of the 32 bit data stream
    #adc_code -= 8388608 #2^23:the only bits we care about
    #adc_voltage=(adc_code*5)/8388608 #conversion from radiometric values
    
