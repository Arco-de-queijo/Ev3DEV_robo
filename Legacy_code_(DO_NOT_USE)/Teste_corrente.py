#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, SpeedPercent, MoveTank, MoveSteering, OUTPUT_A
from ev3dev2.button import Button



MOTORES = LargeMotor(OUTPUT_A)
BTN = Button()



while True:
   MOTORES.on(SpeedPercent(100)*-1,)
