import datetime.datetime as datetime
class LightSensor():
    """
    Class that controls the sensors and actuators for the raspberry pi
    """
    def __init__(self):
        self.pinout={1:'I2C'} #to do:check if we need to change this
        self.name='light_sensor'
    def change_pinout(self,new_pin):
        #change pins based on new pin dict
        #new pin is a new i2c port, either 1, 2 or 3 
        self.pinout={new_pin:'I2C'}
    def read(self):
        """
        Take a single reading from the current point in time
        and gives a time stamp for each sensor as well as the value
        """
        from grovepi.grove_i2c_digital_light_sensor import readVisibleLux
        
        return readVisibleLux