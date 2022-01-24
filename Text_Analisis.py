import constants as cs
import helper as hp


#Definir a que categoria pertenece el texto
def FirstStep(text_input):

    #comprobar si es orden o pregunta
    if '?' in text_input:
        for Temporizacion in cs.TEMP_QUESTIONS:
            for item in Temporizacion:
                if item in text_input:
                    return cs.Categories.TEMPO

    #Comprobar si es una orden especial
    if 'apagate' in text_input:
        return cs.Categories.EXIT
    
    #Comprobar si me piden subir o bajar el volumen
    elif 'volumen' in text_input:
        return cs.Categories.AJUSTES

   
    else:
        #comprobar si hay alguna orden de temporizacion
        for item in cs.TEMPORIZADOR:
            if item in text_input:
                return cs.Categories.TEMPO
            
        #Comprobar si nos están saludando
        for Saludo in cs.SALUDOS:
            if Saludo in text_input:
                return cs.Categories.SALUDO

        #Comprobar si se están despidiendo
        for Despedida in cs.DESPEDIDAS:
            if Despedida in text_input:
                return cs.Categories.DESPEDIDA

    return None