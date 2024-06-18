#!/usr/bin/env python3
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, MoveTank
from ev3dev2.button import Button


from tanq_obj import Tanque

MOTORES = MoveTank(OUTPUT_A, OUTPUT_B)
BTN = Button()
MOVIMENTO = Tanque()


while True:

    MOVIMENTO.speed_a = 50
    MOVIMENTO.speed_b = 50
    MOVIMENTO.padrao()

