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
#from Color_Range import Cores
#from debug_print_function import debug_print

#def Loop_principal():
#variáveis
ativar = Evento()
movimento = Tanque()
#cor = Cores()
voz = Sound()
motores = MoveTank(OUTPUT_A, OUTPUT_B)
#sensorultra1 = UltrasonicSensor(INPUT_1)
sensorultra2 = UltrasonicSensor(INPUT_2)
sensorcor1 = ColorSensor(INPUT_3)
sensorcor2 = ColorSensor(INPUT_4)
btn = Button()
sensorcor1.calibrate_white()
sensorcor2.calibrate_white()



    #loop principal
while True:

            #if (sensorultra1.distance_centimeters <= 6:
                #se o sensor da frente chegar 6cm de um objeto vira para esquerda
                #gira em um raio
                #curva de ~180°

                #ativar.evento_desviar()

        #bloco do sensor de cor para curvas
        #
        #
        #

            if (sensorcor1.color_name == "Green"
            and sensorcor2.color_name != "Green"):
                #vira na direção do verde esquerdo

                ativar.curva_fechada_esq()

            if (sensorcor2.color_name == "Green"
            and sensorcor1.color_name != "Green"):
                #vira na direção do verde direito

                ativar.curva_fechada_dir()


            if (sensorcor1.color_name == "Green"
            and sensorcor2.color_name == "Green"):
                #quando vê dois verdes para de se mover

                motores.off()

                ativar.dar_volta()

        #bloco do sensor de cor para trajeto
        #
        #
        #

            if (sensorcor1.color_name != "Black"
            and sensorcor2.color_name != "Black"):
                #Move o robô para frente

                ativar.acelerar()

            #elif (sensorcor1.color_name == "Black"
            # and sensorcor2.color_name == "Black"):
                #Dá ré e refaz ultimo movimento

            #    ativar.perpendicular_reta()

            if (sensorcor1.color_name == "Black"
            and sensorcor2.color_name != "Black"):
                #Vira para a Direita

                ativar.ajuste_1()

            if (sensorcor1.color_name != "Black"
            and sensorcor2.color_name == "Black"):
                #Vira para a Esquerda

                ativar.ajuste_2()
