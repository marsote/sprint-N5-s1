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

    def extraccion_diario_valida(self, extraccion):
        if extraccion <= self.limite_extraccion_diario and extraccion <= self.monto:
            return True
        else:
            return False

    def transferencia_recibida_valida(self, transferencia):
        if transferencia <= self.limite_monto_transferido:
            return True
        else:
            return False

    def transferencia_emitida_valida(self, transferencia):
        tasa = transferencia * self.porcentaje_comision_trasnferencia / 100
        if transferencia <= self.monto - tasa:
            return True
        else:
            return False

    def puede_crear_chequera(self):
        if self.chequeras <= self.cantidad_maxima_chequeras:
            return True
        else:
            return False

    def puede_crear_tarjeta_debito(self):
        if self.tarjeta_debito <= self.cantidad_tarjeta_debito:
            return True
        else:
            return False
    
    def puede_crear_tarjeta_credito(self):
        if self.tarjeta_credito <= self.cantidad_tarjeta_credito:
            return True
        else:
            return False

    def puede_comprar_dolar(self):
        return self.compra_dolares

    def puede_vender_dolar(self):
        return self.venta_dolares

    """  
    def crearHtml():
        return "html"
    def grabarHtml(self):
        archivo = open('index.html', 'w')
        archivo.write(self.crearHtml) """