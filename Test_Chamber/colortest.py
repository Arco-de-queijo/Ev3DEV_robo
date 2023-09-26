#!/usr/bin/env python3
import time
from ev3dev2.sensor import INPUT_3, INPUT_4
from ev3dev2.motor import MoveSteering
from ev3dev2.sound import Sound
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.button import Button

#variáveis
voz = Sound()
motores = MoveTank(OUTPUT_A, OUTPUT_B)
sensorcor1 = ColorSensor(INPUT_3)
sensorcor2 = ColorSensor(INPUT_4)
btn = Button()
sensorcor1.calibrate_white()
sensorcor2.calibrate_white()


while not btn.any():

    if sensorcor1.color_name == "Green" and not sensorcor2.color_name == "Green":
        #vira na direção do verde esquerdo
                motores.off()
                motores.on_for_rotations(100,100,2)
                motores.on_for_seconds(SpeedPercent(0), SpeedPercent(-100), 1)
                motores.off()
                motores.on_for_seconds(SpeedPercent(-100), SpeedPercent(-100),1)
                motores.off()

    if sensorcor2.color_name == "Green" and not sensorcor1.color_name == "Green":
        #vira na direção do verde direito
                motores.off()
                motores.on_for_rotations(100,100,2)
                motores.on_for_seconds(SpeedPercent(-100), SpeedPercent(0), 1)
                motores.off()
                motores.on_for_seconds(SpeedPercent(-100), SpeedPercent(-100),1)
                motores.off()

    if sensorcor1.color_name == "Green" and sensorcor2.color_name == "Green":
        #quando vê dois verdes para de se mover
                motores.off()

