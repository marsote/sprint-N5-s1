class ProcesadorHtml:
    def __init__(self):
        self.elementos= []
        

    def append(self, elemento):
        self.elementos.append(elemento)

    def crear_html(self, cliente):
        transacciones = ''
        for e in self.elementos:
            transacciones += "<div> {fecha} </div>"

        html = """
            <html>
                <li>Listado de transacciones</li>
            </html>
            """.format(
                direccion=str(cliente.direccion),
                numero=cliente.numero,
                nombre=cliente.nombre
                # agregar
            )
        archivo = open("index.html", "w")
        archivo.write(html)
        archivo.close()
