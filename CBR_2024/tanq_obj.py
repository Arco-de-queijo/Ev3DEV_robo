#!/usr/bin/env python3
#bibliotecas
import time
from ev3dev2.motor import LargeMotor, SpeedPercent, MoveTank, MoveSteering, OUTPUT_A, OUTPUT_B

MOTORES = MoveTank(OUTPUT_A, OUTPUT_B)



class Tanque:

    velocidade_esquerda = 0
    velocidade_direita = 0
    angulo = 0
    rotacao = 0
    segundos = 0

    def padrao(self) -> None:


        MOTORES.on(SpeedPercent(self.velocidade_esquerda)*-1, SpeedPercent(self.velocidade_direita)*-1)


    def angular(self) -> None:

        MOTORES.off()
        MOTORES.on_for_degrees(SpeedPercent(self.velocidade_esquerda)*-1, SpeedPercent(self.velocidade_direita)*-1, (self.angulo))


    def rotacionar(self) -> None:

        MOTORES.off()
        MOTORES.on_for_rotations(SpeedPercent(self.velocidade_esquerda)*-1, SpeedPercent(self.velocidade_direita)*-1, (self.rotacao))


    def tempo(self) -> None:

        MOTORES.off()
        MOTORES.on_for_seconds(SpeedPercent(self.velocidade_esquerda)*-1, SpeedPercent(self.velocidade_direita)*-1, (self.segundos))
