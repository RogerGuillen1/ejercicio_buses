class Bus:
    bus_id = 0

    def __init__(self, plazas):
        Bus.bus_id += 1
        self.plazas = plazas
        self.plazas_iniciales = plazas
        self.billetes = []

    def ventaBilletes(self, plazas, billetes):
        if(billetes > plazas):
            return None
        else:
            return plazas - billetes
        
    def devolucionBilletes(self, plazas, plazas_iniciales, billetes):
        if(billetes > (plazas_iniciales - plazas)):
            return None
        else:
            return plazas + billetes
        
    def plazasVendidas(self, plazas_iniciales, plazas):
        return plazas_iniciales - plazas
    
    def estado(self):
        plazas_vendidas = self.plazasVendidas(self.plazas_iniciales, self.plazas)
        print(f'Quedan {self.plazas} plazas de {self.plazas_iniciales} iniciales y se han vendido {plazas_vendidas} billetes.')
        

