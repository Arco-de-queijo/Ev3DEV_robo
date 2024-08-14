#!/usr/bin/env python3
#bibliotecas
import time
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sound import Sound
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, MoveTank, LargeMotor, MediumMotor
from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor
from ev3dev2.button import Button

#objetos
from tanq_obj import Tanque
from eventos_obj import Evento

ATIVAR = Evento()

VOZ = Sound()
MOTORES = MoveTank(OUTPUT_A, OUTPUT_B)
GARRA_AGARRAR = MediumMotor(OUTPUT_C)
GARRA_MOVER = LargeMotor(OUTPUT_D)
SENSOR_ULTRA1 = UltrasonicSensor(INPUT_2)
SENSOR_COR1 = ColorSensor(INPUT_4)
BTN = Button()
SENSOR_COR1.calibrate_white()


ATIVAR.foo()
