from bus import Bus
from billete import Billete

def pedir_entero_positivo(mensaje):
    while True:
        valor = input(mensaje)
        if valor.isdigit():
            numero = int(valor)
            if numero > 0:
                return numero
            else:
                print("El número debe ser mayor que cero")
        else:
            print("Debes poner un número entero positivo")

plazas = pedir_entero_positivo('Introduce el número de plazas: ')
opcion = None

autobus = Bus(plazas)

while(opcion != 0):
    print('1. Venta de billetes')
    print('2. Devolución de billetes')
    print('3. Estado de la venta')
    print('0. Salir')

    opcion_input = input('Elige una opción: ')

    while not opcion_input.isdigit():
        print("Debes poner un número entero")
        opcion_input = input('Elige una opción: ')
    
    opcion = int(opcion_input)

    if(opcion == 1):
        billetes = pedir_entero_positivo('Número de billetes a vender: ')
        
        plazas_restantes = autobus.ventaBilletes(autobus.plazas, billetes)
        if(plazas_restantes is None):
            print('No hay suficientes plazas disponibles')
        else:            
            for x in range(billetes):
                nombre = input('Nombre del comprador: ')
                apellido = input('Apellido del comprador: ')                
                billete = Billete(nombre, apellido)  
                autobus.billetes.append(billete) 

            autobus.plazas = plazas_restantes
            print(f'Se han vendido {billetes} billetes. Quedan {autobus.plazas} plazas.')
    elif(opcion == 2):
        billetes = pedir_entero_positivo('Número de billetes a devolver: ')

        plazas_restantes = autobus.devolucionBilletes(autobus.plazas, autobus.plazas_iniciales, billetes)
        if(plazas_restantes is None):
            print('No se pueden devolver más billetes de los vendidos')
        else:
            for x in range(billetes):
                if autobus.billetes:  
                    autobus.billetes.pop()

            autobus.plazas = plazas_restantes
            print(f'Se han devuelto {billetes} billetes. Quedan {autobus.plazas} plazas.')
    elif(opcion == 3):
        autobus.estado()
    elif(opcion != 0):
        print('Opción no válida')

print('Has salido del programa...')
