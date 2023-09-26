#!/usr/bin/env python3
import time
from ev3dev2.sensor import INPUT_3, INPUT_4
from ev3dev2.motor import MoveSteering
from ev3dev2.sound import Sound
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.button import Button


voz = Sound()
motores = MoveTank(OUTPUT_A, OUTPUT_B)
sensorluz1 = ColorSensor(INPUT_3)
sensorluz2 = ColorSensor(INPUT_4)
btn = Button()
sensorluz1.calibrate_white()
sensorluz2.calibrate_white()

while not btn.any():
    
    if sensorluz1.reflected_light_intensity >= 30 and sensorluz2.reflected_light_intensity >= 30:
        
            motores.on(SpeedPercent(-50), SpeedPercent(-50))#frente
    
    elif sensorluz1.reflected_light_intensity <= 30 and sensorluz2.reflected_light_intensity <= 30:
        
            motores.off()#Ré
            motores.on(SpeedPercent(50), SpeedPercent(50))
        
    elif sensorluz1.reflected_light_intensity <= 30 and sensorluz2.reflected_light_intensity >= 30:
        
            motores.off()#direita
            motores.on(SpeedPercent(0), SpeedPercent(-50))
            
    elif sensorluz2.reflected_light_intensity <= 30 and sensorluz1.reflected_light_intensity >= 30:
        
            motores.off()#esquerda
            motores.on(SpeedPercent(-50), SpeedPercent(0))