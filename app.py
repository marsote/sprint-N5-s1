from clases import Parser

if __name__ == "__main__":
    parser = Parser()
    cliente = parser.leerDatos('actividades.json')
    print(cliente[0].limite_extraccion_diario)