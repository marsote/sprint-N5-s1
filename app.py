from clases import *

if __name__ == "__main__":
    parser = Parser()
    cliente, transacciones = parser.leerDatos('actividades.json')
    salida = ProcesadorHtml()
    buscador = BuscadorProblema(cliente)
    print(cliente.nombre)
    for e in transacciones:
        print("transaccion: ", e["estado"])
        salida.append(buscador.getResultado(e))

    salida.crear_html(cliente)