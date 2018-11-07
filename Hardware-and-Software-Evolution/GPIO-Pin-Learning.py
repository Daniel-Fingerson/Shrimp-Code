#Written by Daniel Fingerson and Luciana Mendez
#All of this code is compltetely irrelevant to the project: this was the first time we had coded software that direclty controlled hardware
#Therefore, we wrote this code to learn how to talk with a Pi
#We also learned how to represent/manipulate these pins with a GUI (for easier user accesability)

import RPi.GPIO as GPIO #module that allows python to interact with GPIO
GPIO.setmode(GPIO.BCM) #Pins allign with Broadcom chip-specific numbers
GPIO.setwarnings(False)
import time
from tkinter.messagebox import showinfo
from tkinter import Tk, Button, Entry, Label, END,BOTH, LEFT
from tkinter import *
import simplejson


def SetPinMode(setting):
    '''Set specific pin as either IN or OUT'''
    global pin_entry
    pin=pin_entry.get()
    pin=pin.split(',')
    for i in range(len(pin)):
        pin[i]=int(pin[i])
    if setting.lower()=='in':
        GPIO.setup(pin,GPIO.IN)
    if setting.lower()=='out':
        GPIO.setup(pin, GPIO.OUT)
    pin_entry.delete(0,END)


def SetOutput(output):
    ''' Changes pin to an output, while also setting it's voltage as either HIGH or LOW;
    pin may be either a single value or list of values; output can be either as well
'''
    global pin_entry
    pin=pin_entry.get()
    pin=pin.split(',')
    for i in range(len(pin)):
        pin[i]=int(pin[i])
    GPIO.setup(pin, GPIO.OUT)
    if output== 'HIGH':
        GPIO.output(pin, GPIO.HIGH)
    if output== 'LOW':
        GPIO.output(pin,GPIO.LOW)
    pin_entry.delete(0,END)

def CheckVoltage():
    '''Check voltage of givin pin (only if SetPin/Output has been called,
    since setup() must be called on the GPIO channel first
'''
    info=[]
    global pin_entry
    pin=pin_entry.get()
    pin=pin.split(',')
    for i in range(len(pin)):
        pin[i]=int(pin[i])
        info.append("Pin " + str(pin[i]) + " is HIGH")
    pin_entry.delete(0,END)
    showinfo("Voltage",info)

def CheckPinMode():
    'Check the mode type of a given pin; should return if its of type IN, OUT, or ALT[#]'
    info=[]
    global pin_entry
    pin=pin_entry.get()
    pin=pin.split(',')
    for i in range(len(pin)):
        pin[i]=int(pin[i])
        mode= GPIO.gpio_function(i)
        if mode==1:
            info.append("Pin " + str(pin[i]) + " is of type OUT")
        elif mode==0:
            info.append("Pin " + str(pin[i]) + " is of type IN")
        else:
            info.append("Pin " + str(pin[i]) + "is of type ALT[#] ")
    pin_entry.delete(0,END)
    showinfo("Pin Mode",info)

def PrintData():
    for i in range(0,32):
        mode= GPIO.gpio_function(i)
        if mode==1:
            mode="IN"
            GPIO.setup(i,GPIO.IN)
            voltage=GPIO.input(i)
        elif mode==0:
            mode="OUT"
            GPIO.setup(i,GPIO.OUT)
            voltage=GPIO.input(i)
        else:
            mode="ALT[#]"
            voltage='n/a'
        print("Pin " + str(i) + ' is of mode type ' + mode+ ' and voltage ' + str(voltage))

def DataFile():
    pinNum=[]
    mode=[]
    voltage=[]
    for i in range(32):
        pinNum.append(i)
        thisMode=GPIO.gpio_function(i)
        if thisMode==1:
            mode.append("IN")
            GPIO.setup(i,GPIO.IN)
            voltage.append(GPIO.input(i))
        elif thisMode==0:
            mode.append("OUT")
            GPIO.setup(i,GPIO.OUT)
            voltage.append(GPIO.input(i))
        else:
            mode.append("ALT[#]")
            voltage.append(-1)
        
    file=open("data.txt","w")
    simplejson.dump(pinNum,file)
    file.write("\n")
    simplejson.dump(mode,file)
    file.write("\n")
    simplejson.dump(voltage,file)
    file.write("\n")
    file.close()
    total=[]
    for i in range(32):
        total.append("Pin " + str(i) + ",type " + mode[i] + ", voltage " + str(voltage[i]) +"\n")
    showinfo("All data", total)
        


#currently, we cannot check voltages of GPIO channels that do not have the setup() called
#this can be potentially resolved by running a for loop of CheckPinMode, and setting them up based on their mode
#not sure if this would work with modes of ALT[#] types

def ShrimpGUI():
    global pin_entry
    root=Tk()
    root.title("Shrimp GUI Version 1")
    label1=Label(root,text="Pin #")
    pin_entry=Entry(root)
    OnButton=Button(root,text="High volt",command=lambda: SetOutput('HIGH'))
    OffButton=Button(root,text="Low volt",command=lambda: SetOutput('LOW'))
    InButton=Button(root,text="Input",command=lambda: SetPinMode('in'))
    OutButton=Button(root,text="Output",command=lambda: SetPinMode('out'))
    CheckVolt=Button(root,text="Check Voltage",command=CheckVoltage)
    CheckPin=Button(root,text="Check Mode", command=CheckPinMode)
    Show=Button(root,text="Show all data (printed)", command=DataFile)
    label1.grid(row=0, column=0)
    pin_entry.grid(row=0,column=1)
    OnButton.grid(row=1,column=0)
    OffButton.grid(row=1,column=1)
    InButton.grid(row=2,column=0)
    OutButton.grid(row=2,column=1)
    CheckVolt.grid(row=3,column=0)
    CheckPin.grid(row=3,column=1)
    Show.grid(row=4,column=0)
    root.mainloop()
