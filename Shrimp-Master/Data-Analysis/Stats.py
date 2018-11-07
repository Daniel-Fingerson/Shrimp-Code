#Written by Luciana Mendez and Daniel Fingerson
from time import gmtime, strftime, sleep, time
import numpy as np
import matplotlib.pyplot as plt
import random
import math 

#creates data 
def createData (filename,tim,n):
    """Creates data for oxygen levels. Takes in as parameters
    how many logs and how much time between them"""
    file=open(filename,"w+")
    for i in range(n):
        sleep(tim-(time()%tim)) #times loop to do so every x seconds
        dateTime=strftime("%Y-%m-%d %H:%M:%S", gmtime())    #date and time
        dummy=random.uniform(0,2)
        datalog=dateTime+" "+str(dummy)+"\n"
        file.write(datalog)
    file.close()

#graph from date to date 
def turnArray(filename):
    "Turns data into array"
    file=open(filename,"r")
    logs=file.readlines()
    data=list()
    for log in logs:
        log=log.replace("\n","")
        data.append(log)
    file.close()
    return(data)
    
#Analyze dataset
def createDict(filename):
    """Returns dictionary with time:value"""
    data=turnArray(filename)
    d=dict()
    for log in data:
        log=log.split(" ")
        d[log[1]]=log[2]
    return(d)

#Summary of Data
def summary(filename):
    """Returns size, max, min, range of time, average,
    std dev, line graph, histogram"""
    vals=createDict(filename)
    #Size
    size=len(vals)
    #Range of time
    minTime=min(vals)
    maxTime=max(vals)
    #Min and max
    levels=np.array(list(vals.values())).astype(float) #oxygen levels
    maxVal=max(levels)
    minVal=min(levels)
    maxTimeVal=list(vals.keys())[list(vals.values()).index(str(maxVal))]
    minTimeVal=list(vals.keys())[list(vals.values()).index(str(minVal))]
    #Average mean
    totalVal=0
    for i in levels:
        totalVal+=i
    mean=totalVal/size
    #Std. dev
    stdDev=0
    for i in levels:
        std=(i-mean)**2
        stdDev+=std
    stdDev=stdDev/size
    stdDev=math.sqrt(stdDev)
    #Histogram of levels
    histogram=plt.hist(levels)
    #Line graph
    weight=[]
    for i in range(1,181):
        weight.append(i)
    line=plt.plot(weight,levels)
    plt.show()
    print("""The data of size %d taken from %s to %s has a maximum of %f at
    %s and a minimum of %f at %s. The average value is %f, with a standard
    deviation of %f"""%(size,minTime,maxTime,maxVal,maxTimeVal,minVal,minTimeVal,mean,stdDev))
