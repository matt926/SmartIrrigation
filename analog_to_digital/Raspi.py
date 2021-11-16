class Raspi():
    """
    Class that controls the sensors and actuators for the raspberry pi
    """
    def __init__(self):
        self.sensors={} #name of sensor:class
        self.pinout={i+1:None for i in range(40)} #pin:connected to sensor.function ie #to do: add default purpose of pinout so we can determine if wrong
        self.name='raspi'
    def add_sensor(self,sensor_object):
        self.sensors.update({sensor_object.name:sensor_object})
        new_pins={key:f'{sensor_object.name}_{sensor_object.pinout[key]}' for key in sensor_object.pinout.keys()}
        self.pinout.update(new_pins)
    def change_pinout(self,pin_dict):
        #change pins based on new pin dict
        #pin dict is in the form {pin:sensor_object_name_pinfunction}
        self.pinout.update(pin_dict)
    def read(self):
        """
        Take a single reading from the current point in time
        and gives a time stamp for each sensor as well as the value
        """
        read_out={}
        for key in self.sensors:
            read_out.update({key:self.sensors[key].read()})
        return read_out

from LightSensor import LightSensor
import time
#default config as we currently have it setup
my_raspi=Raspi()
my_raspi.add_sensor(LightSensor())
while True:
    print(my_raspi.read())
    time.sleep(60)
