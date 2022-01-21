import time
import constants as cs
from datetime import date, datetime
from typing import NamedTuple


class Temporizador(NamedTuple):
    index: int = 0
    start: int = 0
    end:   int = 0
    name:  str = "default"

#Clase encargada de las acciones relativas al tiempo
class temporizador():
    __meses = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre",
    }

    __dias = {
    0: "lunes",
    1: "martes",
    2: "miércoles",
    3: "jueves",
    4: "viernes",
    5: "sábado",
    6: "domingo",
    }

    def __init__(self):
        self.temporizando = False
        self.N_Temporizadores = 0
        self.Temporizadores = []
        
        return

    def __cronometro(self):
        return

    def __set_timer(self, frase):
        self.temporizando = True
        self.N_Temporizadores += 1

        temp = Temporizador()

        self.Temporizadores.append(temp)
        return

    def bucle_timers(self):

        #Comprobar si alguno de los temporizadores ha terminado
        for temp in self.Temporizadores:
            if time.time() > temp.end:
                self.Temporizadores.remove(temp)
                self.N_Temporizadores -= 1

                #si todos los temporizadores terminan, podemos darlo por finalizao
                if self.N_Temporizadores == 0:
                    self.temporizando = False

                return temp


    
    def __get_actual_date(self):
        today = date.today()
        
        fecha = "Hoy es "
        fecha += self.__dias[int(today.weekday())] + ', ' + str(today.day)
        fecha += ' de ' + self.__meses[int(today.month)]
        fecha += ' del ' + str(today.year) + '.'

        return fecha

    def __get_actual_time(self):
        now = datetime.now()

        hora = now.hour
        if hora > 12:
            hora -= 12

        if hora == 1:
            hora_str = "Es la una y "

        elif hora == 00:
            hora_str = "Son las doce y "
        
        else:
            hora_str = "Son las " + str(hora) + " y "

        hora_str += str(now.minute) + "."

        return hora_str

    def procesa(self, clave, frase):
        resultado = None
        
        if 'hora' in clave:
            return self.__get_actual_time()

        if clave in cs.FECHA:
            return self.__get_actual_date()
        
        if clave in cs.TEMPORIZADOR:
            return self.__set_timer(frase)
        
        return resultado