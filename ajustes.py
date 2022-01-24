import constants as cs
import helper as hp
import pyttsx3

def Volumen(text_input):
    if ' al ' not in text_input:
        cambio = 0
        for item in cs.VOL_UP:
            if item in text_input:
                cambio = 0.1

        for item in cs.VOL_DOWN:
            if item in text_input:
                cambio = -0.1

        volumen = hp.Friday.getProperty('volume') + cambio

        if volumen == 0 or volumen > 1:
            return

        if cs.DEVELOPMENT:
            print('Cambiando el volumen de '+str(volumen) + ' ' + str(volumen - cambio))
        else:
            hp.Friday.setProperty('volume', volumen)
            hp.Friday.runAndWait()
            hp.Friday.stop()

    else:
        startindex = text_input.rfind(' al ') +4
        endindex = str(text_input).find(' ', startindex)
        if endindex == -1:
            endindex = len(text_input)

        substring = text_input[startindex:endindex]
        volumen = float(int(substring) / 10)

        if cs.DEVELOPMENT:
            print('Cambiando el volumen a '+ str(volumen))
        else:
            hp.Friday.setProperty('volume', volumen)
            hp.Friday.runAndWait()
            hp.Friday.stop()
        
    return   