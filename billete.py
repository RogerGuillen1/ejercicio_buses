from persona import Persona

class Billete:
    __billete_id = 0
    def __init__(self, pNombre, pApellido):
        self.__persona = Persona(pNombre, pApellido)
        Billete.__billete_id += 1

    def getBilleteId(self):
        return self.__billete_id
    
    def __str__(self):
        return self.__persona

