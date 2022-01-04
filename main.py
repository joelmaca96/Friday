import pyttsx3
import constants as cs

global Friday


def inicializar():
    global Friday
    Friday = pyttsx3.init()

    Friday.setProperty('rate', 130)

def Preprocesado(input):
    #Eliminar tildes
    for a, b in cs.tildes:
        input = input.replace(a, b).replace(a.upper(), b.upper())

    #Eliminar mayusculas
    output =  input.lower()

    return output

def Say(speech):
    Friday.say(speech) 
    Friday.runAndWait() 
    Friday.stop()

def Ajustes(input):
    for item in cs.VOL_UP:
            if item in input:
                if 'al' not in input:
                    volumen = Friday.getProperty('volume')
                    if volumen < 1:
                        print('Subiendo el volumen de '+str(volumen) + ' ' + str(volumen + 0.1))
                        Friday.setProperty('volume', volumen + 0.1)
                        Friday.runAndWait() 
                        Friday.stop()
                return

    for item in cs.VOL_DOWN:
        if item in input:
            if 'al' not in input:
                volumen = Friday.getProperty('volume')
                if volumen > 0.2:
                    print('bajando el volumen de '+str(volumen) + ' ' + str(volumen - 0.1))
                    Friday.setProperty('volume', volumen - 0.1)
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
