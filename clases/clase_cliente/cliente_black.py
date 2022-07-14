from .cliente import Cliente

class ClienteBlack(Cliente):
    def __init__(self, **kwargs):
        super(ClienteBlack, self).__init__(**kwargs)
