import importlib
from .clase_cliente import Cliente
from .clase_razon import Razon
from .transaccion import Transaccion

class BuscadorProblema:
    def __init__(self, cliente: Cliente):
    
        self.cliente = cliente
        self.tipos = {
            "RETIRO_EFECTIVO_CAJERO_AUTOMATICO":{
                "modulo": "raz_retiro_efectivo",
                "clase": "RazonRetiroEfectivo"
            },
            "ALTA_RARJETA_CREDITO":{
                "modulo": "raz_alta_t_credito",
                "clase": "RazonRetiroEfectivo"
            },
            "ALTA_CHEQUERA":{
                "modulo": "raz_alta_chequera",
                "clase": "RazonRetiroEfectivo"
            },
            "COMPRAR_DOLAR":{
                "modulo": "raz_comprar_dolar",
                "clase": "RazonRetiroEfectivo"
            },
            "TRANSFERENCIA_ENVIADA":{
                "modulo": "raz_transferencia_enviada",
                "clase": "RazonRetiroEfectivo"
            },
            "TRANSFERENCIA_RECIBIDA":{
                "modulo": "raz_transferencia_recibida",
                "clase": "RazonRetiroEfectivo"
            }

        }
    
    def getResultado(self, transaccion):
        explicacion = ""
        if transaccion['estado'] == Transaccion.RECHAZADA:
            module = importlib.import_module("."+ self.tipos[transaccion['tipo']]['modulo'],"clases.clase_razon")
            razon = getattr(module, self.tipos[transaccion['tipo']]['clase'])()
            explicacion = razon.resolver(self.cliente, transaccion)

        return{
            "razon": explicacion,
            "estado": transaccion['estado'],
            "tipo": transaccion['tipo'],
            "saldo": transaccion['saldoEnCuenta'],
            "fecha":transaccion['fecha'],
            "monto": transaccion['monto']
        }