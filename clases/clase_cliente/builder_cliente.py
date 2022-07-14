class BuilderCliente:
    def __init__(self):
        pass
    @staticmethod
    def getDatosClientesClassic():
        return{
            "limite_extraccion_diario":10000,
            "cantidad_tarjeta_debito":1,
            "cantidad_tarjeta_credito":0,
            "cantidad_caja_ahorro_pesos":1,
            "cantidad_caja_ahorro_dolares":0,
            "cantidad_cuenta_corriente_pesos":0,
            "descubierto_cuenta_corriente":0,
            "cantidad_maxima_chequeras":0,
            "limite_monto_transferido":150000,
            "compra_dolares":False,
            "venta_dolares":False,
            "porcentaje_comision_transferencia":1
        }
    
    @staticmethod
    def getDatosClientesGold():
        return{
            "limite_extraccion_diario":20000,
            "cantidad_tarjeta_debito":1,
            "cantidad_tarjeta_credito":1,
            "cantidad_caja_ahorro_pesos":1,
            "cantidad_caja_ahorro_dolares":1,
            "cantidad_cuenta_corriente_pesos":1,
            "descubierto_cuenta_corriente":10000,
            "cantidad_maxima_chequeras":1,
            "limite_monto_transferido":500000,
            "compra_dolares":True,
            "venta_dolares":True,
            "porcentaje_comision_transferencia":0.5
        }
        
    @staticmethod
    def getDatosClientesBlack():
        return{
            "limite_extraccion_diario":100000,
            "cantidad_tarjeta_debito":1,
            "cantidad_tarjeta_credito":5,
            "cantidad_caja_ahorro_pesos":1,
            "cantidad_caja_ahorro_dolares":1,
            "cantidad_cuenta_corriente_pesos":1,
            "descubierto_cuenta_corriente":10000,
            "cantidad_maxima_chequeras":2,
            "limite_monto_transferido":"infinito",
            "compra_dolares":True,
            "venta_dolares":True,
            "porcentaje_comision_transferencia":0
        }