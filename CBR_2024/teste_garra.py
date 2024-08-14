#!/usr/bin/env python3
#bibliotecas
import time
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sound import Sound
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, MoveTank, LargeMotor, MediumMotor
from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor
from ev3dev2.button import Button

from claw_obj import Claw_class

GARRA = Claw_class()


GARRA.velocidade = 100
GARRA.angulo = 1200
GARRA.agarrar_angular()

GARRA.velocidade = 50
GARRA.angulo = -90
GARRA.mover_angular()

time.sleep(5)

GARRA.velocidade = 30
GARRA.angulo = 90
GARRA.mover_angular()

GARRA.velocidade = 25
GARRA.angulo = -1200
GARRA.agarrar_angular()
