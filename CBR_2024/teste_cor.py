#!/home/robot/venv311/bin/python3.11
#bibliotecas
import time
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from debug_print_function import debug_print
from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor



SENSOR_COR1 = ColorSensor(INPUT_4)


SENSOR_COR1.calibrate_white()

while True:

    debug_print(SENSOR_COR1.rgb)
