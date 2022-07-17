from .cliente import Cliente

class ClienteBlack(Cliente):
    def __init__(self, **kwargs):
        super(ClienteBlack, self).__init__(**kwargs)
    def puede_crear_chequera(self):
        return True
    def puede_crear_tarjeta_credito(self):
        return True
    def puede_comprar_dolar(self):
        return True