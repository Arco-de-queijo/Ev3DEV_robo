#!/usr/bin/env python3
#bibliotecas
import time
import sys
from ev3dev2.sensor import INPUT_3, INPUT_4, INPUT_1, INPUT_2
from ev3dev2.sound import Sound
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank, MoveSteering
from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor
from ev3dev2.button import Button

#objetos e funções
from tanq_obj import Tanque
from debug_print_function import debug_print

#variáveis
movimento = Tanque()
voz = Sound()
motores = MoveTank(OUTPUT_A, OUTPUT_B)
sensorultra1 = UltrasonicSensor(INPUT_1)
sensorultra2 = UltrasonicSensor(INPUT_2)
sensorcor1 = ColorSensor(INPUT_3)
sensorcor2 = ColorSensor(INPUT_4)
btn = Button()
sensorcor1.calibrate_white()
sensorcor2.calibrate_white()

listared1= []
listagreen1= []
listablue1= []
voz.beep(2)
time.sleep(5)

while not btn.any():



    colorlist1 = list(sensorcor1.rgb)
    red1, green1, blue1 = colorlist1

    listared1.append(red1)
    listagreen1.append(green1)
    listablue1.append(blue1)

    if len(listared1) >= 10:

        debug_print(listared1)
        debug_print(listagreen1)
        debug_print(listablue1)
        break
