#!/usr/bin/env python3
#bibliotecas
import time
from ev3dev2.motor import LargeMotor, SpeedPercent, MoveTank, MoveSteering, OUTPUT_A, OUTPUT_B

MOTORES = MoveTank(OUTPUT_A, OUTPUT_B)



class Tanque:

    speed_a: float | int = 0
    speed_b: float | int = 0
    angulo: float | int = 0
    rotacao: float | int = 0
    segundos: float | int = 0

    def padrao(self) -> None:


        MOTORES.on(SpeedPercent(self.speed_a)*-1, SpeedPercent(self.speed_b)*-1)


    def angular(self) -> None:

        MOTORES.off()
        MOTORES.on_for_degrees(SpeedPercent(self.speed_a)*-1, SpeedPercent(self.speed_b)*-1, (self.angulo) )


    def rotacionar(self) -> None:

        MOTORES.off()
        MOTORES.on_for_rotations(SpeedPercent(self.speed_a)*-1, SpeedPercent(self.speed_b)*-1, (self.rotacao) )


    def tempo(self) -> None:

        MOTORES.off()
        MOTORES.on_for_seconds(SpeedPercent(self.speed_a)*-1, SpeedPercent(self.speed_b)*-1, (self.segundos) )
