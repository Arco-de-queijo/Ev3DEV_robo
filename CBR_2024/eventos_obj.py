#!/usr/bin/env python3
#bibliotecas
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor
from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_B

#objetos
from tanq_obj import Tanque
from claw_obj import Claw_class
MOTORES = MoveTank(OUTPUT_A, OUTPUT_B)

MOVIMENTO = Tanque()
GARRA = Claw_class()
SENSOR_ULTRA1 = UltrasonicSensor(INPUT_2)
SENSOR_COR1 = ColorSensor(INPUT_4)



class Evento:

    def foo(self) -> None:
        GARRA.velocidade = 100
        GARRA.rotacao = 1
        GARRA.agarrar_rotacionar()

    def bar(self) -> None:
        GARRA.velocidade = 100
        GARRA.rotacao = 1
        GARRA.mover_rotacionar()


    def curva_fechada_esq(self) -> None:

        MOVIMENTO.velocidade_esquerda = -100
        MOVIMENTO.velocidade_direita = -100
        MOVIMENTO.rotacao = 0.75
        MOVIMENTO.rotacionar()


        MOVIMENTO.velocidade_esquerda = -100
        MOVIMENTO.velocidade_direita = 100
        MOVIMENTO.rotacao = 1.5
        MOVIMENTO.rotacionar()

        MOVIMENTO.velocidade_esquerda = 100
        MOVIMENTO.velocidade_direita = 100
        MOVIMENTO.rotacao = 1.5
        MOVIMENTO.rotacionar()

    def curva_fechada_dir(self) -> None:

        MOVIMENTO.velocidade_esquerda = 100
        MOVIMENTO.velocidade_direita = -100
        MOVIMENTO.rotacao = 1.5
        MOVIMENTO.rotacionar()

        MOVIMENTO.velocidade_esquerda = 100
        MOVIMENTO.velocidade_direita = 100
        MOVIMENTO.rotacao = 1.5
        MOVIMENTO.rotacionar()

    def acelerar(self) -> None:

        MOVIMENTO.velocidade_esquerda = 50
        MOVIMENTO.velocidade_direita = 50
        MOVIMENTO.padrao()

    def ajuste_para_direita(self) -> None:

        MOVIMENTO.velocidade_esquerda = 60
        MOVIMENTO.velocidade_direita = -60
        MOVIMENTO.rotacao = 0.125
        MOVIMENTO.rotacionar()
        MOTORES.off()

    def ajuste_para_esquerda(self) -> None:

        MOVIMENTO.velocidade_esquerda = -60
        MOVIMENTO.velocidade_direita = 60
        MOVIMENTO.rotacao = 0.125
        MOVIMENTO.rotacionar()
        MOTORES.off()
