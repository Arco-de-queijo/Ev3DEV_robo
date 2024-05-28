#!/usr/bin/env python3
#bibliotecas
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor
from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_B

#objetos
from tanq_obj import Tanque
MOTORES = MoveTank(OUTPUT_A, OUTPUT_B)

#variáveis
MOVIMENTO = Tanque()
#sensorultra1 = UltrasonicSensor(INPUT_1)
SENSOR_ULTRA2 = UltrasonicSensor(INPUT_2)
SENSOR_COR1 = ColorSensor(INPUT_3)
SENSOR_COR2 = ColorSensor(INPUT_4)

class Evento:
    volantemem: int = 0


    def evento_desviar(self) -> None:
        angulogiro: float | int = 0

        MOVIMENTO.speed_a = -100
        MOVIMENTO.speed_b = 100
        MOVIMENTO.rotacao = 1.5
        MOVIMENTO.rotacionar()


        caixaloop: str = "on"

        while caixaloop == "on":
        #se vira a direita em um raio



            if SENSOR_ULTRA2.distance_centimeters > 15:

                MOVIMENTO.speed_a = 100
                MOVIMENTO.speed_b = -100
                MOVIMENTO.rotacao = 0.01
                MOVIMENTO.rotacionar()

                angulogiro += 1

            else:

                MOVIMENTO.speed_a = 100
                MOVIMENTO.speed_b = 100
                MOVIMENTO.padrao()


            if angulogiro >= 180:
                caixaloop = "off"
                while True:

                    MOVIMENTO.speed_a = 70
                    MOVIMENTO.speed_b = 70
                    MOVIMENTO.padrao()

                    if SENSOR_COR1.color_name == "Black" or SENSOR_COR2.color_name != "Black":

                        MOVIMENTO.speed_a = -100
                        MOVIMENTO.speed_b = 100
                        MOVIMENTO.rotacao = 1.5
                        MOVIMENTO.rotacionar()
                        break


    def curva_fechada_esq(self) -> None:

        MOVIMENTO.speed_a = -100
        MOVIMENTO.speed_b = -100
        MOVIMENTO.rotacao = 0.3
        MOVIMENTO.rotacionar()


        MOVIMENTO.speed_a = -100
        MOVIMENTO.speed_b = 100
        MOVIMENTO.rotacao = 1.5
        MOVIMENTO.rotacionar()

        MOVIMENTO.speed_a = 100
        MOVIMENTO.speed_b = 100
        MOVIMENTO.rotacao = 1
        MOVIMENTO.rotacionar()

        self.volantemem = 1

    def curva_fechada_dir(self) -> None:

        MOVIMENTO.speed_a = -100
        MOVIMENTO.speed_b = -100
        MOVIMENTO.rotacao = 0.3
        MOVIMENTO.rotacionar()


        MOVIMENTO.speed_a = 100
        MOVIMENTO.speed_b = -100
        MOVIMENTO.rotacao = 1.5
        MOVIMENTO.rotacionar()

        MOVIMENTO.speed_a = 100
        MOVIMENTO.speed_b = 100
        MOVIMENTO.rotacao = 1
        MOVIMENTO.rotacionar()

        self.volantemem = 2

    def dar_volta(self) -> None:

        MOVIMENTO.speed_a = 100
        MOVIMENTO.speed_b = -100
        MOVIMENTO.rotacao = 3
        MOVIMENTO.rotacionar()

        MOVIMENTO.speed_a = 100
        MOVIMENTO.speed_b = 100
        MOVIMENTO.rotacao = 1
        MOVIMENTO.rotacionar()




    def perpendicular_reta(self) -> None:

        if self.volantemem == 2:


            MOVIMENTO.speed_a = -100
            MOVIMENTO.speed_b = 100
            MOVIMENTO.rotacao = 1
            MOVIMENTO.rotacionar()

        elif self.volantemem == 1:


            MOVIMENTO.speed_a = 100
            MOVIMENTO.speed_b = -100
            MOVIMENTO.rotacao = 1
            MOVIMENTO.rotacionar()

    def acelerar(self) -> None:

        MOVIMENTO.speed_a = 100
        MOVIMENTO.speed_b = 100
        MOVIMENTO.padrao()

    def ajuste_1(self) -> None:


            MOVIMENTO.speed_a = 0
            MOVIMENTO.speed_b = -100
            MOVIMENTO.rotacao = 0.5
            MOVIMENTO.rotacionar()

            MOVIMENTO.speed_a = -100
            MOVIMENTO.speed_b = 0
            MOVIMENTO.rotacao = 1
            MOVIMENTO.rotacionar()

            MOVIMENTO.speed_a = 100
            MOVIMENTO.speed_b = 100
            MOVIMENTO.rotacao = 0.4
            MOVIMENTO.rotacionar()

            self.volantemem = 2

    def ajuste_2(self) -> None:



            MOVIMENTO.speed_a = -100
            MOVIMENTO.speed_b = 0
            MOVIMENTO.rotacao = 0.5
            MOVIMENTO.rotacionar()

            MOVIMENTO.speed_a = 0
            MOVIMENTO.speed_b = -100
            MOVIMENTO.rotacao = 1
            MOVIMENTO.rotacionar()

            MOVIMENTO.speed_a = 100
            MOVIMENTO.speed_b = 100
            MOVIMENTO.rotacao = 0.4
            MOVIMENTO.rotacionar()


            self.volantemem = 1

