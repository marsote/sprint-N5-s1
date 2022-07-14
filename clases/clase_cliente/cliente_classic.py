from .cliente import Cliente

class ClienteClassic(Cliente):
    def __init__(self, **kwargs):
        super(ClienteClassic, self).__init__(**kwargs)

    def puede_crear_chequera(self):
        return False

    