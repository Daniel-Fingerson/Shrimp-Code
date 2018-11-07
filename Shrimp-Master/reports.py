# Module: reports.py
#Daniel Fingerson added the variable "spoof" to try and better handle an explicit real/fake data switch
from bokeh.driving import linear
from bokeh.layouts import column
from bokeh.server.server import Server

import sensor as s


#some sort of conditional needs to occur where if a button is pressed, the state of spoof changes
def sensorInit(sensorArray,spoof=0):#spoof determines whether sensors are fed real or fake data (demonstartion purposes)
    """Initializes all sensors to be used."""
    sensorArray.append(s.Sensor("Oxygen", "mg/l", spoof,
                                lambda x: x, "red", 6.67))
    sensorArray.append(s.Sensor("Nitrogen", "mg/l", spoof,
                                lambda x: x, "blue", 29.67))


def sensorLoop(sensorArray):
    """Updates data for every sensor"""
    for sensor in sensorArray:
        sensor.getData()


def modifyDoc(doc): #spoof choice must be implemented here 
    """Creates the live Bokeh plot"""
    sensorArray = []
    sensorInit(sensorArray,-1)

    @linear()
    def update(step):
        """Updates for live data stream in browser"""
        sensorLoop(sensorArray)
        for sensor in sensorArray:
            sensor.updatePlot(step)

    for sensor in sensorArray:
        doc.add_root(column(sensor.plot))

    doc.add_periodic_callback(update, 500)


def bokehLoop():
    """Runs the Bokeh server in the background"""
    server = Server({'/reports': modifyDoc},
                    allow_websocket_origin=["localhost:8000"])
    server.start()
    server.io_loop.start()
