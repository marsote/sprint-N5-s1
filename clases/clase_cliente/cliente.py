from ..clase_cuenta.cuenta import Cuenta
from ..clase_direccion import Direccion


CLASSIC = "CLASSIC"
GOLD = "GOLD"
BLACK = "BLACK"

class Cliente(Cuenta):
    def __init__(self, **kwargs):
        self.cuenta = Cuenta(**kwargs)

    def inicializar(self, datos):
        self.numero = datos["numero"]
        self.nombre = datos["nombre"]
        self.apellido = datos["apellido"]
        self.dni = datos["dni"]
        self.direccion = Direccion(**datos["direccion"])

    """  
    def crearHtml():
        return "html"
    def grabarHtml(self):
        archivo = open('index.html', 'w')
        archivo.write(self.crearHtml) """