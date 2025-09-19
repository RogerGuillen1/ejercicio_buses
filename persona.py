class Persona:
    def __init__(self, pNombre, pApellido):
        self.__nombre = pNombre
        self.__apellido = pApellido
    def getNombre(self):
        return self.__nombre
    def getNombre(self):
        return self.__nombre
    def setNombre(self, pNombre):
        self.__nombre = pNombre
    def setApellido(self, pApellido):
        self.__apellido = pApellido
    def __str__(self):
        return f'Billete de {self.__nombre} {self.__apellido}'
