import time
import keyboard


print("     MODOS:\n\n\n")



while True:
    tecla = keyboard.read_event()
    tecla.event_type = keyboard.KEY_DOWN

    print("|||INICIAR|||                  CALIBRAR", end='\r')

    if tecla.name == 'l'():

        print("INICIAR                  |||CALIBRAR|||", end='\r')

        while not tecla.name =='r':
            print("INICIAR                  |||CALIBRAR|||", end='\r')
