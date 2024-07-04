
class Cliente:
    def __init__(self, id_cliente, nombre, correo, telefono):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.pedidos = []

    def agregar_pedido(self, pedido):
        self.pedidos.append(pedido)

    def obtener_cantidad_pedidos(self):
        return len(self.pedidos)

    def __str__(self):
        return f"Cliente: {self.nombre} (ID: {self.id_cliente})"
