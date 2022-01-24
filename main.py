import helper as hp
import pyttsx3
import constants as cs
import threading
import time
import ajustes
from temporizador import temporizador as temp

global tempo
global exit
global text_input
global new_text

def inicializar():
    global tempo
    global exit, text_input, new_text
    
    new_text = False
    text_input = None
    exit = False

    #arrancar el modulo de temporizacion
    tempo = temp()

def get_data(args):
    global exit, text_input, new_text
    while not exit:
        if not new_text:
            text_input = input("Enter the text: ")
            text_input = hp.Preprocesado(text_input)
            new_text = True
        
        else:
            time.sleep(0.1)
    return

def rutina_principal(args):
    in_conversation = False
    global exit, text_input, new_text

    while not exit:
        if new_text:
            if not in_conversation and text_input != None :
                if cs.NAME in text_input:
                    #Inicio conversacion.
                    in_conversation = True

            if in_conversation:
                #Comprobar si es una orden especial
                if 'apagate' in text_input:
                    exit = True
                
                #Comprobar si me piden subir o bajar el volumen
                if 'volumen' in text_input:
                    ajustes.Volumen(text_input)

                #comprobar si hay alguna orden de temporizacion
                for Temporizacion in cs.TEMP_CONSTANTS:
                    found = False
                    for item in Temporizacion:
                        if item in text_input:
                            hp.Say(tempo.procesa(item, text_input))
                            found = True
                            break
                    if found:
                        break
                    
                #Comprobar si nos están saludando
                for Saludo in cs.SALUDOS:
                    if Saludo in text_input:
                        hp.Say("Buenos días!")
                        break

                #Comprobar si se están despidiendo
                for Despedida in cs.DESPEDIDAS:
                    if Despedida in text_input:
                        hp.Say("Agur.")
                        in_conversation = False
                    break
            new_text = False
        else:
            time.sleep(0.1)
    return

if __name__ == "__main__":
    
    inicializar()

    #Arrancar las tareas
    MainTask    = threading.Thread(target=rutina_principal, args=(1,))
    GetDataTask = threading.Thread(target=get_data, args=(1,))

    MainTask.start()
    GetDataTask.start()



