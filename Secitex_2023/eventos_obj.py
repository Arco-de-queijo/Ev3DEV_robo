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


class Evento:
    volantemem = 0


    def evento_desviar(self):
        angulogiro = 0

        movimento.speed_a = -100
        movimento.speed_b = 100
        movimento.rotacao = 1.5
        movimento.rotacionar()

        movimento.speed_a = 100
        movimento.speed_b = 100
        movimento.rotacao = 0.5
        movimento.rotacionar()

        caixaloop = "on"

        while caixaloop == "on":
        #se vira a direita em um raio



            if sensorultra2.distance_centimeters > 25:

                movimento.speed_a = 100
                movimento.speed_b = -100
                movimento.rotacao = 0.01
                movimento.rotacionar()

                angulogiro += 1

            else:

                movimento.speed_a = 100
                movimento.speed_b = 100
                movimento.padrao()


            if angulogiro >= 120:
                caixaloop = "off"

                if sensorultra2.distance_centimeters <= 25:

                    movimento.speed_a = -100
                    movimento.speed_b = 100
                    movimento.rotacao = 1.5
                    movimento.rotacionar()


                    angulogiro = 0
                else:
                    self.volantemem = 2
                    angulogiro = 0
                    break

    def curva_fechada_esq(self):


        movimento.speed_a = -100
        movimento.speed_b = 100
        movimento.rotacao = 1.5
        movimento.rotacionar()

        movimento.speed_a = 100
        movimento.speed_b = 100
        movimento.rotacao = 1.5
        movimento.rotacionar()

        self.volantemem = 1

    def curva_fechada_dir(self):


        movimento.speed_a = 100
        movimento.speed_b = -100
        movimento.rotacao = 1.5
        movimento.rotacionar()

        movimento.speed_a = 100
        movimento.speed_b = 100
        movimento.rotacao = 1.5
        movimento.rotacionar()

        self.volantemem = 2

    def perpendicular_reta(self):

        movimento.speed_a = -50
        movimento.speed_b = -50
        movimento.padrao()

        if self.volantemem == 2:

            movimento.speed_a = -100
            movimento.speed_b = -100
            movimento.rotacao = 0.75
            movimento.rotacionar()

            movimento.speed_a = -100
            movimento.speed_b = 100
            movimento.rotacao = 1.5
            movimento.rotacionar()

        elif self.volantemem == 1:

            movimento.speed_a = -100
            movimento.speed_b = -100
            movimento.rotacao = 0.75
            movimento.rotacionar()

            movimento.speed_a = 100
            movimento.speed_b = -100
            movimento.rotacao = 1.5
            movimento.rotacionar()

    def acelerar(self):

        movimento.speed_a = 50
        movimento.speed_b = 50
        movimento.padrao()

    def ajuste_para_direita(self):

        movimento.speed_a = 60
        movimento.speed_b = -60
        movimento.rotacao = 0.125
        movimento.rotacionar()
        motores.off()

        self.volantemem = 2

    def ajuste_para_esquerda(self):

        movimento.speed_a = -60
        movimento.speed_b = 60
        movimento.rotacao = 0.125
        movimento.rotacionar()
        motores.off()

        self.volantemem = 1

