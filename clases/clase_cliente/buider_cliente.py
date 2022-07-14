""" class BuilderCliente:
    def __init__(self):
        pass
    @staticmethod
    def getDatosClientesClassic():
        return{
            "limite_extraccion_diario:":1000,
            "limite_extraccion_mensual:":10000,
            "limite_extraccion_anual:":100000
        }
    
    @staticmethod
    def getDatosClientesGold():
        return{
            "limite_extraccion_diario:":2000,
            "limite_extraccion_mensual:":20000,
            "limite_extraccion_anual:":200000
        }
        
    @staticmethod
    def getDatosClientesBlack():
        return{
            "limite_extraccion_diario:":3000,
            "limite_extraccion_mensual:":30000,
            "limite_extraccion_anual:":300000
        } """