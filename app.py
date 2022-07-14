from clases import Parser

if __name__ == "__main__":
    parser = Parser()
    cliente = parser.leerDatos('entregaSprint/actividades.json')
    print(cliente)