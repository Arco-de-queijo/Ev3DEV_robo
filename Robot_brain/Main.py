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

def Loop_principal():
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
    nome_cor1 = cor.Sensor_1()
    nome_cor2 = cor.Sensor_2()
    sensorcor1.calibrate_white()
    sensorcor2.calibrate_white()



    #loop principal
    while True:
            colorlist1 = list(sensorcor1.rgb)
            colorlist2 = list(sensorcor2.rgb)
            cor.red1, cor.green1, cor.blue1 = colorlist1
            cor.red2, cor.green2, cor.blue2 = colorlist2


        #bloco do sonar

            if sensorultra1.distance_centimeters <= 6:
                #se o sensor da frente chegar 6cm de um objeto vira para esquerda
                #gira em um raio
                #curva de ~180°

                ativar.evento_desviar()

        #bloco do sensor de cor para curvas

            if nome_cor1 == "Verde"  :
                #vira na direção do verde esquerdo

                motores.off()

                if nome_cor2 == "Verde":
                    break

                else:
                    ativar.curva_fechada_esq()

            if nome_cor2 == "Verde":
                #vira na direção do verde direito

                motores.off()

                if nome_cor1 == "Verde":
                    break

                else:
                    ativar.curva_fechada_dir()


            if nome_cor1 == "Verde" and nome_cor2 == "Verde":
                #quando vê dois verdes para de se mover

                motores.off()
                break

        #bloco do sensor de cor para trajeto

            if nome_cor1 != "Preto" and nome_cor2 != "Preto":
                #Move o robô para frente

                ativar.acelerar()

            elif nome_cor1 == "Preto" and nome_cor2 == "Preto":
                #Dá ré e refaz ultimo movimento

                ativar.perpendicular_reta()

            elif nome_cor1 == "Preto" and nome_cor2 != "Preto":
                #Vira para a Direita

                ativar.ajuste_para_direita()

            elif nome_cor2 == "Preto" and nome_cor1 != "Preto":
                #Vira para a Esquerda

                ativar.ajuste_para_esquerda()
