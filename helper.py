import pyttsx3
import constants as cs

print(' importando friday')
Friday = pyttsx3.init()
Friday.setProperty('rate', 130) 

def Preprocesado(text_input):
    #Eliminar tildes
    for a, b in cs.tildes:
        text_input = text_input.replace(a, b).replace(a.upper(), b.upper())

    #Eliminar mayusculas
    output =  text_input.lower()

    return output


def Say(speech):
    if cs.DEVELOPMENT:
        print(speech)
    else:
        Friday.say(speech) 
        Friday.runAndWait() 
        Friday.stop()