#!/usr/bin/env python3
import ast

path = "color_range.txt"

with open(path, "r") as file:

    linha = file.readlines()
    #primeiro sensor
    r_verde_1 = linha [0]
    g_verde_1 = linha [1]
    b_verde_1 = linha [2]

    r_preto_1 = linha [4]
    g_preto_1 = linha [5]
    b_preto_1 = linha [6]

    r_cinza_1 = linha [8]
    g_cinza_1 = linha [9]
    b_cinza_1 = linha [10]


    r_verde_2 = linha [12]
    g_verde_2 = linha [13]
    b_verde_2 = linha [14]

    r_preto_2 = linha [16]
    g_preto_2 = linha [17]
    b_preto_2 = linha [18]

    r_cinza_2 = linha [20]
    g_cinza_2 = linha [21]
    b_cinza_2 = linha [22]



    lista_r_verde_1 = ast.literal_eval(r_verde_1)
    lista_g_verde_1 = ast.literal_eval(g_verde_1)
    lista_b_verde_1 = ast.literal_eval(b_verde_1)

    lista_r_preto_1 = ast.literal_eval(r_preto_1)
    lista_g_preto_1 = ast.literal_eval(g_preto_1)
    lista_b_preto_1 = ast.literal_eval(b_preto_1)

    lista_r_cinza_1 = ast.literal_eval(r_cinza_1)
    lista_g_cinza_1 = ast.literal_eval(g_cinza_1)
    lista_b_cinza_1 = ast.literal_eval(b_cinza_1)

    lista_r_verde_2 = ast.literal_eval(r_verde_2)
    lista_g_verde_2 = ast.literal_eval(g_verde_2)
    lista_b_verde_2 = ast.literal_eval(b_verde_2)

    lista_r_preto_2 = ast.literal_eval(r_preto_2)
    lista_g_preto_2 = ast.literal_eval(g_preto_2)
    lista_b_preto_2 = ast.literal_eval(b_preto_2)

    lista_r_cinza_2 = ast.literal_eval(r_cinza_2)
    lista_g_cinza_2 = ast.literal_eval(g_cinza_2)
    lista_b_cinza_2 = ast.literal_eval(b_cinza_2)


class Cores():

    red1 = 0
    green1 = 0
    blue1 = 0

    red2 = 0
    green2 = 0
    blue2 = 0




    def Sensor_1(self):


        if (self.red1 in range(min(lista_r_verde_1), max(lista_r_verde_1)+1)
        and self.green1 in range(min(lista_g_verde_1), max(lista_g_verde_1)+1)
        and self.blue1 in range(min(lista_b_verde_1), max(lista_b_verde_1)+1)):

            return "Verde"

        if (self.red1 in range(min(lista_r_preto_1), max(lista_r_preto_1)+1)
        and self.green1 in range(min(lista_g_preto_1), max(lista_g_preto_1)+1)
        and self.blue1 in range(min(lista_b_preto_1), max(lista_b_preto_1)+1)):

            return "Preto"

        if (self.red1 in range(min(lista_r_cinza_1), max(lista_r_cinza_1)+1)
        and self.green1 in range(min(lista_g_cinza_1), max(lista_g_cinza_1)+1)
        and self.blue1 in range(min(lista_b_cinza_1), max(lista_b_cinza_1)+1)):

            return "Cinza"

        else:
            return "None"


    def Sensor_2(self):

        if (self.red2 in range(min(lista_r_verde_2), max(lista_r_verde_2)+1)
        and self.green2 in range(min(lista_g_verde_2), max(lista_g_verde_2)+1)
        and self.blue2 in range(min(lista_b_verde_2), max(lista_b_verde_2)+1)):

            return "Verde"

        if (self.red2 in range(min(lista_r_preto_2), max(lista_r_preto_2)+1)
        and self.green2 in range(min(lista_g_preto_2), max(lista_g_preto_2)+1)
        and self.blue2 in range(min(lista_b_preto_2), max(lista_b_preto_2)+1)):

            return "Preto"

        if (self.red2 in range(min(lista_r_cinza_2), max(lista_r_cinza_2)+1)
        and self.green2 in range(min(lista_g_cinza_2), max(lista_g_cinza_2)+1)
        and self.blue2 in range(min(lista_b_cinza_2), max(lista_b_cinza_2)+1)):

            return "Cinza"

        else:
            return "None"
