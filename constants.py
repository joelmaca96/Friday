from enum import Enum

#Constantes para Friday
NAME = 'friday'
TEMPORIZADOR = ['temporizador', 'cuenta', 'cronometra', 'alarma', 'avisame']
HORA = ['hora']
FECHA = ['fecha', 'dia']
OPERACIONES = ['mas', 'menos', 'entre', 'dividido por', 'multiplicado por', 'por']

TEMP_QUESTIONS = [HORA, FECHA]
VOL_UP = ['sube', 'subir', 'eleva', 'aumenta']
VOL_DOWN = ['baja', 'bajar', 'disminuye', 'reduce']
SALUDOS = ['hola', 'buenos dias', 'buenas tardes', 'kaixo', 'egun on', 'buenas noches', 'ole']
DESPEDIDAS = ['adios', 'hasta luego', 'que tengas un buen dia', 'calla', 'agur', 'aio', 'hasta pronto', 'callate', 'que te den']

#Categorias de texto
class Categories(Enum):
    EXIT      = 1
    AJUSTES   = 2
    TEMPO     = 3
    SALUDO    = 4
    DESPEDIDA = 5


#Substituciones para el preprocesado del texto
tildes = (
    ("á", "a"),
    ("é", "e"),
    ("í", "i"),
    ("ó", "o"),
    ("ú", "u"),
)

#Maquina de estados
STARTING   =  0
IDLE       =  5
PROCESANDO = 10
ESPERANDO  = 15

#Ajustes para la ejecucion
DEVELOPMENT = True
