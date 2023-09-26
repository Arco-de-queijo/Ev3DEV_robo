#!/usr/bin/env python3
import time
from ev3dev2.sensor import INPUT_3, INPUT_4
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.button import Button
from debug_print_function import debug_print

sensorcor1 = ColorSensor(INPUT_3)

sensorcor1.calibrate_white()

voz=Sound()

colorlist1 = []
voz.beep()
time.sleep(5)

colorlist1 = list(sensorcor1.rgb)

debug_print(colorlist1)
