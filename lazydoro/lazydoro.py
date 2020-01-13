# Simple demo of the VL53L0X distance sensor.
# Will print the sensed range/distance every second.
import time

import board
import busio

import adafruit_vl53l0x

# Initialize I2C bus and sensor.
i2c = busio.I2C(board.SCL, board.SDA)
vl53 = adafruit_vl53l0x.VL53L0X(i2c)

class Pomodoro:
    def __init__(self):
        self.state = 'waiting'



# Main loop will check the range and
while True:
    print('Range: {0}mm'.format(vl53.range))
    time.sleep(1.0)