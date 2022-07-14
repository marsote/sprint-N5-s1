class Validacion:
    def __init__(self, cliente, parametros):
        self.cliente = cliente
        self.parametros = parametros

    

    def validarClassic(self):
        if self.parametros["cantidad_tarjeta_debito"] > 1:
            raise Exception("Solo puede tener una tarjeta de debito")
        if self.parametros["cantidad_tarjeta_credito"] > 0:
            raise Exception("No puede tener tarjeta de credito")
        if self.parametros["cantidad_caja_ahorro_pesos"] > 1:
            raise Exception("Solo puede tener una caja de ahorro en pesos")
        if self.parametros["cantidad_caja_ahorro_dolares"] > 0:
            raise Exception("No puede tener caja de ahorro en dolares")
        if self.parametros["cantidad_cuenta_corriente_pesos"] > 0:
            raise Exception("No puede tener cuenta corriente en pesos")
        if self.parametros["descubierto_cuenta_corriente"] > 0:
            raise Exception("No puede tener descubierto en cuenta corriente")
        if self.parametros["cantidad_maxima_chequeras"] > 0:
            raise Exception("No puede tener chequeras")
        if self.parametros["limite_monto_transferido"] > 150000:
            raise Exception("No puede tener un limite de transferencia mayor a 150.000")
        if self.parametros["compra_dolares"] == True:
            raise Exception("No puede tener compra en dolares")
        if self.parametros["venta_dolares"] == True:
            raise Exception("No puede tener venta en dolares")
        if self.parametros["porcentaje_comision_transferencia"] > 1:
            raise Exception("No puede tener un porcentaje de comision mayor a 1")