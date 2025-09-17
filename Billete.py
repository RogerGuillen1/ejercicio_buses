from Persona import Persona

class Billete:
    billete_id = 0
    def __init__(self, pNombre, pApellido):
        self.__persona = Persona(pNombre, pApellido)
        self.__billete_id = self.__billete_id+1
    def getBilleteId():
        return self.__billete_id
    def __str__():
        return self.__persona

