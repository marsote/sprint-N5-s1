class Cuenta:
    def __init__(self, **kwargs):
        self.limite_extraccion_diario = kwargs.get("limite_extraccion_diario", 0)
