class Cuenta:
    def __init__(self, **kwargs):
        
        self.limite_extraccion_diario = kwargs.get("limite_extraccion_diario", 0)
        self.limite_transferencia_recibida = kwargs.get("limite_transferencia_recibida", 0)
        self.porcentaje_comision_trasnferencia = kwargs.get("porcentaje_comision_transferencia", 0)
        self.descubierto_desponible = kwargs.get("descubierto_desponible", 0)
        self.cantidad_tarjeta_credito = kwargs.get("cantidad_tarjeta_credito", 0)
        self.cantidad_maxima_chequeras = kwargs.get("cantidad_maxima_chequeras", 0)

        # self.cantidad_tarjeta_debito = kwargs.get("cantidad_tarjeta_debito", 0)
        # self.cantidad_caja_ahorro_pesos = kwargs.get("cantidad_caja_ahorro_pesos", 0)
        # self.cantidad_caja_ahorro_dolares = kwargs.get("cantidad_caja_ahorro_dolares", 0)
        # self.cantidad_cuenta_corriente_pesos = kwargs.get("cantidad_cuenta_corriente_pesos", 0)
        # self.compra_dolares = kwargs.get("compra_dolares", False)
        # self.venta_dolares = kwargs.get("venta_dolares", False)
        