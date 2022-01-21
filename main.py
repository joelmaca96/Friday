import pyttsx3
import constants as cs
import threading
import time
from temporizador import temporizador as temp

global Friday
global tempo
global exit
global text_input
global new_text
DEVELOPMENT = True

def inicializar():
    global Friday, tempo
    global exit, text_input
    
    text_input = None
    exit = False

    Friday = pyttsx3.init()

    Friday.setProperty('rate', 130)

    #arrancar el modulo de temporizacion
    tempo = temp()

def Preprocesado(text_input):
    #Eliminar tildes
    for a, b in cs.tildes:
        text_input = text_input.replace(a, b).replace(a.upper(), b.upper())

    #Eliminar mayusculas
    output =  text_input.lower()

    return output

def Say(speech):
    if DEVELOPMENT:
        print(speech)
    else:
        Friday.say(speech) 
        Friday.runAndWait() 
        Friday.stop()

def Ajustes(text_input):
    if ' al ' not in text_input:
        cambio = 0
        for item in cs.VOL_UP:
            if item in text_input:
                cambio = 0.1

        for item in cs.VOL_DOWN:
            if item in text_input:
                cambio = -0.1

        volumen = Friday.getProperty('volume') + cambio

        if volumen == 0 or volumen > 1:
            return

        if DEVELOPMENT:
            print('Cambiando el volumen de '+str(volumen) + ' ' + str(volumen - cambio))
        else:
            Friday.setProperty('volume', volumen)
            Friday.runAndWait()
            Friday.stop()

    else:
        startindex = text_input.rfind(' al ') +4
        endindex = str(text_input).find(' ', startindex)
        if endindex == -1:
            endindex = len(text_input)

        substring = text_input[startindex:endindex]
        volumen = float(int(substring) / 10)

        if DEVELOPMENT:
            print('Cambiando el volumen a '+ str(volumen))
        else:
            Friday.setProperty('volume', volumen)
            Friday.runAndWait()
            Friday.stop()
        
    return   

def get_data(args):
    global exit, text_input, new_text
    while not exit:
        if not new_text:
            text_input = input("Enter the text: ")
            text_input = Preprocesado(text_input)
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
                    Ajustes(text_input)

                #comprobar si hay alguna orden de temporizacion
                for Temporizacion in cs.TEMP_CONSTANTS:
                    found = False
                    for item in Temporizacion:
                        if item in text_input:
                            Say(tempo.procesa(item))
                            found = True
                            break
                    if found:
                        break
                    
                #Comprobar si nos están saludando
                for Saludo in cs.SALUDOS:
                    if Saludo in text_input:
                        Say("Buenos días!")
                        break

                #Comprobar si se están despidiendo
                for Despedida in cs.DESPEDIDAS:
                    if Despedida in text_input:
                        Say("Agur.")
                        in_conversation = False
                    break
        
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



