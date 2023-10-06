#!/usr/bin/env python3
#bibliotecas
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor
from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_B

#objetos
from tanq_obj import Tanque
motores = MoveTank(OUTPUT_A, OUTPUT_B)

#variáveis
movimento = Tanque()
sensorultra1 = UltrasonicSensor(INPUT_1)
sensorultra2 = UltrasonicSensor(INPUT_2)
sensorcor1 = ColorSensor(INPUT_3)
sensorcor2 = ColorSensor(INPUT_4)


class Evento:
    volantemem = 0


    def evento_desviar(self):
        angulogiro = 0

        movimento.speed_a = -100
        movimento.speed_b = 100
        movimento.rotacao = 1.5
        movimento.rotacionar()


        caixaloop = "on"

        while caixaloop == "on":
        #se vira a direita em um raio



            if sensorultra2.distance_centimeters > 15:

                movimento.speed_a = 100
                movimento.speed_b = -100
                movimento.rotacao = 0.01
                movimento.rotacionar()

                angulogiro += 1

            else:

                movimento.speed_a = 100
                movimento.speed_b = 100
                movimento.padrao()


            if angulogiro >= 180:
                caixaloop = "off"
                while True:

                    movimento.speed_a = 70
                    movimento.speed_b = 70
                    movimento.padrao()

                    if sensorcor1.color_name == "Black" or sensorcor2.color_name != "Black":

                        movimento.speed_a = -100
                        movimento.speed_b = 100
                        movimento.rotacao = 1.5
                        movimento.rotacionar()
                        break


    def curva_fechada_esq(self):

        movimento.speed_a = -100
        movimento.speed_b = -100
        movimento.rotacao = 0.3
        movimento.rotacionar()


        movimento.speed_a = -100
        movimento.speed_b = 100
        movimento.rotacao = 1.5
        movimento.rotacionar()

        movimento.speed_a = 100
        movimento.speed_b = 100
        movimento.rotacao = 1
        movimento.rotacionar()

        self.volantemem = 1

    def curva_fechada_dir(self):

        movimento.speed_a = -100
        movimento.speed_b = -100
        movimento.rotacao = 0.3
        movimento.rotacionar()


        movimento.speed_a = 100
        movimento.speed_b = -100
        movimento.rotacao = 1.5
        movimento.rotacionar()

        movimento.speed_a = 100
        movimento.speed_b = 100
        movimento.rotacao = 1
        movimento.rotacionar()

        self.volantemem = 2

    def dar_volta(self):

        movimento.speed_a = 100
        movimento.speed_b = -100
        movimento.rotacao = 3
        movimento.rotacionar()

        movimento.speed_a = 100
        movimento.speed_b = 100
        movimento.rotacao = 1
        movimento.rotacionar()




    def perpendicular_reta(self):

        if self.volantemem == 2:


            movimento.speed_a = -100
            movimento.speed_b = 100
            movimento.rotacao = 1
            movimento.rotacionar()

        elif self.volantemem == 1:


            movimento.speed_a = 100
            movimento.speed_b = -100
            movimento.rotacao = 1
            movimento.rotacionar()

    def acelerar(self):

        movimento.speed_a = 100
        movimento.speed_b = 100
        movimento.padrao()

    def ajuste_1(self):


            movimento.speed_a = 0
            movimento.speed_b = -100
            movimento.rotacao = 0.5
            movimento.rotacionar()

            movimento.speed_a = -100
            movimento.speed_b = 0
            movimento.rotacao = 1
            movimento.rotacionar()

            movimento.speed_a = 100
            movimento.speed_b = 100
            movimento.rotacao = 0.4
            movimento.rotacionar()

            self.volantemem = 2

    def ajuste_2(self):



            movimento.speed_a = -100
            movimento.speed_b = 0
            movimento.rotacao = 0.5
            movimento.rotacionar()

            movimento.speed_a = 0
            movimento.speed_b = -100
            movimento.rotacao = 1
            movimento.rotacionar()

            movimento.speed_a = 100
            movimento.speed_b = 100
            movimento.rotacao = 0.4
            movimento.rotacionar()


            self.volantemem = 1

