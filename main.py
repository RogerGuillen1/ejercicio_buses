from bus import Bus

plazas = int(input('Introduce el número de plazas: '))
opcion = None

autobus1 = Bus(plazas)

while(opcion != 0):
    print('1. Venta de billetes')
    print('2. Devolución de billetes')
    print('3. Estado de la venta')
    print('0. Salir')

    opcion = int(input('Elige una opción: '))

    if(opcion == 1):
        billetes = int(input('Número de billetes a vender: '))
        plazas_restantes = autobus1.ventaBilletes(autobus1.plazas, billetes)
        if(plazas_restantes is None):
            print('No hay suficientes plazas disponibles')
        else:
            nombre = input('Nombre del comprador: ')
            apellido = input('Apellido del comprador: ')
            
                

            autobus1.plazas = plazas_restantes
            print(f'Se han vendido {billetes} billetes. Quedan {autobus1.plazas} plazas.')
    # elif(opcion == 2):

    # elif(opcion == 3):

    # else:
    #     print('Opción no válida')


print('Has salido del programa...')
