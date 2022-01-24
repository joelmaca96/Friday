import helper as hp
import pyttsx3
import constants as cs
import threading
import time
import ajustes
from Text_Analisis import FirstStep
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
    last_interaction = time.time()
    global exit, text_input, new_text

    while not exit:

        if new_text:
            last_interaction = time.time()
            if not in_conversation and text_input != None :
                if cs.NAME in text_input:
                    #Inicio conversacion.
                    in_conversation = True

            if in_conversation:
                categoria = FirstStep(text_input)

                if categoria == cs.Categories.EXIT:
                    exit = True
                
                elif categoria == cs.Categories.AJUSTES:
                    ajustes.Volumen(text_input)
                
                elif categoria == cs.Categories.TEMPO :
                    hp.Say(tempo.procesa(text_input))

                elif categoria == cs.Categories.SALUDO:
                    hp.Say("Buenos días!")
                
                elif categoria == cs.Categories.DESPEDIDA:
                    hp.Say("Agur.")
                    in_conversation = False

            new_text = False

        #si pasan mas de 30 segundos sin interaccion, damos por terminada la conversacion
        elif in_conversation:
            if time.time() - last_interaction > 30:
                hp.Say("Hasta luego!")
                in_conversation = False
        
        time.sleep(0.1)
    return

if __name__ == "__main__":
    inicializar()

    #Arrancar las tareas
    MainTask    = threading.Thread(target=rutina_principal, args=(1,))
    GetDataTask = threading.Thread(target=get_data, args=(1,))

    MainTask.start()
    GetDataTask.start()



