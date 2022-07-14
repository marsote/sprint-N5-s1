from .cliente import Cliente

class ClienteGold(Cliente):
    def __init__(self, **kwargs):
        super(ClienteGold, self).__init__(**kwargs)
