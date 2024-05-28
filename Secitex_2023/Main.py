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
ATIVAR = Evento()
MOVIMENTO = Tanque()
#cor = Cores()
VOZ = Sound()
MOTORES = MoveTank(OUTPUT_A, OUTPUT_B)
#sensorultra1 = UltrasonicSensor(INPUT_1)
SENSOR_ULTRA2 = UltrasonicSensor(INPUT_2)
SENSOR_COR1 = ColorSensor(INPUT_3)
SENSOR_COR2 = ColorSensor(INPUT_4)
BTN = Button()
SENSOR_COR1.calibrate_white()
SENSOR_COR2.calibrate_white()



    #loop principal
while True:

            #if (sensorultra1.distance_centimeters <= 6:
                #se o sensor da frente chegar 6cm de um objeto vira para esquerda
                #gira em um raio
                #curva de ~180°

                #ATIVAR.evento_desviar()

        #bloco do sensor de cor para curvas
        #
        #
        #

            if (SENSOR_COR1.color_name == "Green"
            and SENSOR_COR2.color_name != "Green"):
                #vira na direção do verde esquerdo

                ATIVAR.curva_fechada_esq()

            if (SENSOR_COR2.color_name == "Green"
            and SENSOR_COR1.color_name != "Green"):
                #vira na direção do verde direito

                ATIVAR.curva_fechada_dir()


            if (SENSOR_COR1.color_name == "Green"
            and SENSOR_COR2.color_name == "Green"):
                #quando vê dois verdes para de se mover

                MOTORES.off()

                ATIVAR.dar_volta()

        #bloco do sensor de cor para trajeto
        #
        #
        #

            if (SENSOR_COR1.color_name != "Black"
            and SENSOR_COR2.color_name != "Black"):
                #Move o robô para frente

                ATIVAR.acelerar()

            #elif (SENSOR_COR1.color_name == "Black"
            # and SENSOR_COR2.color_name == "Black"):
                #Dá ré e refaz ultimo movimento

            #    ATIVAR.perpendicular_reta()

            if (SENSOR_COR1.color_name == "Black"
            and SENSOR_COR2.color_name != "Black"):
                #Vira para a Direita

                ATIVAR.ajuste_1()

            if (SENSOR_COR1.color_name != "Black"
            and SENSOR_COR2.color_name == "Black"):
                #Vira para a Esquerda

                ATIVAR.ajuste_2()
