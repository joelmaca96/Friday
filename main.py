import pyttsx3
import constants as cs
from temporizador import temporizador as temp
global Friday
global tempo
DEVELOPMENT = True

def inicializar():
    global Friday, tempo
    Friday = pyttsx3.init()

    Friday.setProperty('rate', 130)

    #arrancar el modulo de temporizacion
    tempo = temp()

def Preprocesado(input):
    #Eliminar tildes
    for a, b in cs.tildes:
        input = input.replace(a, b).replace(a.upper(), b.upper())

    #Eliminar mayusculas
    output =  input.lower()

    return output

def Say(speech):
    if DEVELOPMENT:
        print(speech)
    else:
        Friday.say(speech) 
        Friday.runAndWait() 
        Friday.stop()

def Ajustes(input):
    if ' al ' not in input:
        cambio = 0
        for item in cs.VOL_UP:
            if item in input:
                cambio = 0.1

        for item in cs.VOL_DOWN:
            if item in input:
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
        startindex = input.rfind(' al ') +4
        endindex = str(input).find(' ', startindex)
        if endindex == -1:
            endindex = len(input)

        substring = input[startindex:endindex]
        volumen = float(int(substring) / 10)

        if DEVELOPMENT:
            print('Cambiando el volumen a '+ str(volumen))
        else:
            Friday.setProperty('volume', volumen)
            Friday.runAndWait()
            Friday.stop()
        
    return   

inicializar()

exit = False
while not exit:
    my_text = input("Enter the text: ")
    my_text = Preprocesado(my_text)

    if cs.NAME in my_text:
        #Comprobar si es una orden especial
        if 'apagate' in my_text:
            exit = True
        
        #Comprobar si me piden subir o bajar el volumen
        if 'volumen' in my_text:
           Ajustes(my_text)

        #comprobar si hay alguna orden de temporizacion
        for Temporizacion in cs.TEMPORIZADOR:
            if Temporizacion in my_text:
                tempo.procesa(my_text)
            
        #Comprobar si nos están saludando
        for Saludo in cs.SALUDOS:
            if Saludo in my_text:
                Say("Buenos días!")
                break

        #Comprobar si se están despidiendo
        for Despedida in cs.DESPEDIDAS:
            if Despedida in my_text:
                Say("Agur.")
                break
