#!/usr/bin/env python3
#bibliotecas
import time
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sound import Sound
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, MoveTank
from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor
from ev3dev2.button import Button

#objetos
from tanq_obj import Tanque
from eventos_obj import Evento
from Color_Range import Cores
from debug_print_function import debug_print

#def Loop_principal():
#variáveis
ativar = Evento()
movimento = Tanque()
cor = Cores()
voz = Sound()
motores = MoveTank(OUTPUT_A, OUTPUT_B)
sensorultra1 = UltrasonicSensor(INPUT_1)
sensorultra2 = UltrasonicSensor(INPUT_2)
sensorcor1 = ColorSensor(INPUT_3)
sensorcor2 = ColorSensor(INPUT_4)
btn = Button()
sensorcor1.calibrate_white()
sensorcor2.calibrate_white()



    #loop principal
while True:
            colorlist1 = list(sensorcor1.rgb)
            colorlist2 = list(sensorcor2.rgb)
            cor.red1, cor.green1, cor.blue1 = colorlist1
            cor.red2, cor.green2, cor.blue2 = colorlist2

            nome_cor1 = cor.Sensor_1()
            nome_cor2 = cor.Sensor_2()
            debug_print(nome_cor1)
            debug_print(nome_cor2)
