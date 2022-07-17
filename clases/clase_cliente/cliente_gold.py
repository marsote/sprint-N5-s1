from .cliente import Cliente

class ClienteGold(Cliente):
    def __init__(self, **kwargs):
        super(ClienteGold, self).__init__(**kwargs)
    
    def puede_crear_chequera(self):
        return True
    def puede_crear_tarjeta_credito(self):
        return True
    def puede_comprar_dolar(self):
        return True