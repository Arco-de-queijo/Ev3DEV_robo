#!/usr/bin/env python3
#bibliotecas
import time
from ev3dev2.motor import LargeMotor, SpeedPercent, MoveTank, MoveSteering, OUTPUT_A, OUTPUT_B

MOTORES = MoveTank(OUTPUT_A, OUTPUT_B)



class Tanque:

    speed_a=0
    speed_b=0
    angulo=0
    rotacao=0
    segundos=0

    def padrao(self):


        MOTORES.on(SpeedPercent(self.speed_a)*-1, SpeedPercent(self.speed_b)*-1)


    def angular(self):

        MOTORES.off()
        MOTORES.on_for_degrees(SpeedPercent(self.speed_a)*-1, SpeedPercent(self.speed_b)*-1, (self.angulo) )


    def rotacionar(self):

        MOTORES.off()
        MOTORES.on_for_rotations(SpeedPercent(self.speed_a)*-1, SpeedPercent(self.speed_b)*-1, (self.rotacao) )


    def tempo(self):

        MOTORES.off()
        MOTORES.on_for_seconds(SpeedPercent(self.speed_a)*-1, SpeedPercent(self.speed_b)*-1, (self.segundos) )
