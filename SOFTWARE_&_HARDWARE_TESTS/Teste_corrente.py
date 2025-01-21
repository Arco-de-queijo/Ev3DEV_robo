#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, SpeedPercent, OUTPUT_A, OUTPUT_B

MOTOR_A = LargeMotor(OUTPUT_A)
MOTOR_B = LargeMotor(OUTPUT_B)

while True:
   MOTOR_A.on(SpeedPercent(100),)
   MOTOR_B.on(SpeedPercent(100),)
