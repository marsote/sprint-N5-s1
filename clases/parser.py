import json
from typing import Tuple
from .clase_cliente import Cliente, ClienteClassic, ClienteGold, ClienteBlack, BuilderCliente


class Parser:

    def leerDatos(self, filename: str):
        transacciones = []
        with open(filename) as jsonFile:
            eventos = json.load(jsonFile)
            cliente = self.parserClientes(eventos)

            for e in eventos["transacciones"]:
                transacciones.append(e)

        return (cliente, transacciones)

    def parserClientes(self, eventos) -> Cliente:
        tipo = eventos["tipo"]

        if tipo == 'CLASSIC':
            cliente = ClienteClassic(
                **BuilderCliente.getDatosClientesClassic())

        elif tipo == 'GOLD':
            cliente = ClienteGold(**BuilderCliente.getDatosClientesClassic())

        elif tipo == 'BLACK':
            cliente = ClienteBlack(**BuilderCliente.getDatosClientesClassic())

        return cliente
