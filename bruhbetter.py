#!/usr/bin/env python3
import time
import sys

from ev3dev2.sound import Sound
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_3, INPUT_4
from ev3dev2.button import Button
from debug_print_function import debug_print


voz = Sound()
motor = LargeMotor(OUTPUT_A)
sensor1 = ColorSensor(INPUT_3)
sensor2 = ColorSensor(INPUT_4)
btn = Button()



while not btn.any():
    debug_print(sensor1.rgb, sensor1.color_name, sensor2.rgb, sensor2.color_name)
