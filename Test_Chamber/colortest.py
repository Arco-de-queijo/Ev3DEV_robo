#!/usr/bin/env python3
import time
from ev3dev2.sensor import INPUT_3, INPUT_4
from ev3dev2.motor import MoveSteering
from ev3dev2.sound import Sound
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.button import Button
from debug_print_function import debug_print

#variáveis
voz = Sound()
motores = MoveTank(OUTPUT_A, OUTPUT_B)
sensorcor1 = ColorSensor(INPUT_3)
sensorcor2 = ColorSensor(INPUT_4)
btn = Button()
sensorcor1.calibrate_white()
sensorcor2.calibrate_white()


while True:
    debug_print("SENSOR 1")
    debug_print(sensorcor1.color_name)

    time.sleep(1)

    debug_print("SENSOR 2")
    debug_print(sensorcor2.color_name)

    time.sleep(1)




