#!/usr/bin/env python3
#bibliotecas
import time
from ev3dev2.motor import LargeMotor, SpeedPercent, MoveTank, MoveSteering, MediumMotor, OUTPUT_C, OUTPUT_D

GARRA_AGARRAR = MediumMotor(OUTPUT_C)
GARRA_MOVER = LargeMotor(OUTPUT_D)



class Claw_class:

    velocidade = 0
    rotacao = 0
    angulo = 0
    segundos = 0

    def agarrar_padrao(self) -> None:

        GARRA_AGARRAR.on(SpeedPercent(self.velocidade))

    def mover_padrao(self) -> None:

        GARRA_MOVER.on(SpeedPercent(self.velocidade))




    def agarrar_angular(self) -> None:

        GARRA_AGARRAR.on_for_degrees(SpeedPercent(self.velocidade), (self.angulo))

    def mover_angular(self) -> None:

        GARRA_MOVER.on_for_degrees(SpeedPercent(self.velocidade), (self.angulo))




    def agarrar_rotacionar(self) -> None:

        GARRA_AGARRAR.on_for_rotations(SpeedPercent(self.velocidade), (self.rotacao))

    def mover_rotacionar(self) -> None:

        GARRA_MOVER.on_for_rotations(SpeedPercent(self.velocidade), (self.rotacao))




    def agarrar_tempo(self) -> None:

        GARRA_AGARRAR.on_for_seconds(SpeedPercent(self.velocidade), (self.segundos))

    def mover_tempo(self) -> None:

        GARRA_MOVER.on_for_seconds(SpeedPercent(self.velocidade), (self.segundos))
