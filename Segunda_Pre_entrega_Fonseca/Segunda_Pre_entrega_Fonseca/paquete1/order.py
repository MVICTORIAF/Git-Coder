
class Pedido:
    def __init__(self, id_pedido, cliente, articulos):
        self.id_pedido = id_pedido
        self.cliente = cliente
        self.articulos = articulos
        self.monto_total = sum(articulo.precio for articulo in articulos)

    def __str__(self):
        return f"Pedido: {self.id_pedido} para {self.cliente.nombre}"
