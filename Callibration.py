#!/usr/bin/env python3
import os
os.environ['TERM'] = 'linux'
def clear_console():
    os.system('clear')
import time
from ev3dev2.sensor import INPUT_3, INPUT_4
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.button import Button


def Calibragem():

    btn = Button()
    voz = Sound()
    sensorcor1 = ColorSensor(INPUT_3)
    sensorcor2 = ColorSensor(INPUT_4)
    sensorcor1.calibrate_white()
    sensorcor2.calibrate_white()
    path = 'color_range.txt'

    listared1= []
    listagreen1= []
    listablue1= []

    listared2= []
    listagreen2= []
    listablue2= []

    #Calibragem para o sensor 1
    #Verde
    voz.beep()
    clear_console()

    print("          |||VERDE|||        ", end='\r')
    btn.wait_for_bump('enter')
    voz.beep(), voz.beep()
    time.sleep(5)

    while True:

        colorlist1 = list(sensorcor1.rgb)
        red1, green1, blue1 = colorlist1

        listared1.append(red1)
        listagreen1.append(green1)
        listablue1.append(blue1)

        if len(listared1) >= 10:
            with open(path, 'r') as file:
                linha = file.readlines()

                linha[0] = '{}\n'.format (listared1)
                linha[1] = '{}\n'.format (listagreen1)
                linha[2] = '{}\n'.format (listablue1)

            with open(path, 'w') as file:
                file.writelines(linha)
            break


    #Preto
    listared1 = []
    listagreen1 = []
    listablue1 = []

    voz.beep()
    clear_console()

    print("          |||PRETO|||        ", end='\r')
    btn.wait_for_bump('enter')
    voz.beep(), voz.beep()
    time.sleep(5)

    while True:
        colorlist1 = list(sensorcor1.rgb)
        red1, green1, blue1 = colorlist1

        listared1.append(red1)
        listagreen1.append(green1)
        listablue1.append(blue1)

        if len(listared1) >= 10:
            with open(path, 'r') as file:
                linha = file.readlines()

                linha[4] = '{}\n'.format (listared1)
                linha[5] = '{}\n'.format (listagreen1)
                linha[6] = '{}\n'.format (listablue1)

            with open(path, 'w') as file:
                file.writelines(linha)
            break

    #Cinza
    listared1 = []
    listagreen1 = []
    listablue1 = []

    voz.beep()
    clear_console()

    print("          |||CINZA|||        ", end='\r')
    btn.wait_for_bump('enter')
    voz.beep(), voz.beep()
    time.sleep(5)

    while True:
        colorlist1 = list(sensorcor1.rgb)
        red1, green1, blue1 = colorlist1

        listared1.append(red1)
        listagreen1.append(green1)
        listablue1.append(blue1)

        if len(listared1) >= 10:
            with open(path, 'r') as file:
                linha = file.readlines()

                linha[8] = '{}\n'.format (listared1)
                linha[9] = '{}\n'.format (listagreen1)
                linha[10] = '{}\n'.format (listablue1)

            with open(path, 'w') as file:
                file.writelines(linha)
            break
    voz.beep(), voz.beep(), voz.beep()


    #segundo sensor
    voz.beep()
    clear_console()

    print("          |||VERDE|||        ", end='\r')
    btn.wait_for_bump('enter')
    voz.beep(), voz.beep()
    time.sleep(5)

    while True:

        colorlist2 = list(sensorcor2.rgb)
        red2, green2, blue2 = colorlist2

        listared2.append(red2)
        listagreen2.append(green2)
        listablue2.append(blue2)

        if len(listared2) >= 10:
            with open(path, 'r') as file:
                linha = file.readlines()

                linha[12] = '{}\n'.format (listared2)
                linha[13] = '{}\n'.format (listagreen2)
                linha[14] = '{}\n'.format (listablue2)

            with open(path, 'w') as file:
                file.writelines(linha)
            break


    #Preto
    listared2 = []
    listagreen2 = []
    listablue2 = []

    voz.beep()
    clear_console()

    print("          |||PRETO|||        ", end='\r')
    btn.wait_for_bump('enter')
    voz.beep(), voz.beep()
    time.sleep(5)

    while True:
        colorlist2 = list(sensorcor2.rgb)
        red2, green2, blue2 = colorlist2

        listared2.append(red2)
        listagreen2.append(green2)
        listablue2.append(blue2)

        if len(listared2) >= 10:
            with open(path, 'r') as file:
                linha = file.readlines()

                linha[16] = '{}\n'.format (listared2)
                linha[17] = '{}\n'.format (listagreen2)
                linha[18] = '{}\n'.format (listablue2)

            with open(path, 'w') as file:
                file.writelines(linha)
            break

    #Cinza
    listared2 = []
    listagreen2 = []
    listablue2 = []

    voz.beep()
    clear_console()

    print("          |||CINZA|||        ", end='\r')
    btn.wait_for_bump('enter')
    voz.beep(), voz.beep()
    time.sleep(5)

    while True:
        colorlist2 = list(sensorcor2.rgb)
        red2, green2, blue2 = colorlist2

        listared2.append(red2)
        listagreen2.append(green2)
        listablue2.append(blue2)

        if len(listared2) >= 10:
            with open(path, 'r') as file:
                linha = file.readlines()

                linha[20] = '{}\n'.format (listared2)
                linha[21] = '{}\n'.format (listagreen2)
                linha[22] = '{}\n'.format (listablue2)

            with open(path, 'w') as file:
                file.writelines(linha)
            break
    voz.beep()
