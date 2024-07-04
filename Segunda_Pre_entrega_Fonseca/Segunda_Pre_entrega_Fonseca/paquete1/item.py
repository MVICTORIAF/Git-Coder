
class Articulo:
    def __init__(self, id_articulo, nombre, precio):
        self.id_articulo = id_articulo
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Articulo: {self.nombre} (ID: {self.id_articulo}) - ${self.precio}"
