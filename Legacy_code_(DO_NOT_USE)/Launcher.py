#!/usr/bin/env python3
#bibliotecas
import os
os.chmod('color_range.txt', 0o777)
os.environ['TERM'] = 'linux'
def clear_console():
    os.system('clear')

import time
from ev3dev2.sensor import INPUT_3, INPUT_4
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.button import Button

from Main import Loop_principal
from Callibration import Calibragem

btn = Button()
voz = Sound()
sensorcor1 = ColorSensor(INPUT_3)
sensorcor2 = ColorSensor(INPUT_4)


voz.beep(5)

while True:
    clear_console()
    print("MODOS:\n\n\n")

    print("   |||INICIAR|||               CALIBRAR", end='\r')

    if btn.enter:

        voz.beep(2), voz.beep(2)
        time.sleep(5)
        clear_console()
        Loop_principal()

    if btn.right:
        clear_console()
        voz.beep(2)
        print("MODOS:\n\n\n")

        print("   INICIAR               |||CALIBRAR|||", end='\r')

        while not btn.left:
            if btn.enter:
                voz.beep(2), voz.beep(2)
                time.sleep(2)
                clear_console()
                Calibragem()

                clear_console()
                voz.beep(2)
                print("MODOS:\n\n\n")

                print("   INICIAR               |||CALIBRAR|||", end='\r')

        voz.beep(2)
