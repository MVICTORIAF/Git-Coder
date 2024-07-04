
from client import Cliente
from order import Pedido
from item import Articulo

def main():
    # Crear algunos artículos
    articulo1 = Articulo(1, "Laptop", 1000)
    articulo2 = Articulo(2, "Mouse", 50)
    articulo3 = Articulo(3, "Teclado", 80)

    # Crear un cliente
    cliente = Cliente(1, "Maria victoria ", "vickifon@hotmail.com", "2357895")

    # Crear un pedido para el cliente
    pedido = Pedido(1, cliente, [articulo1, articulo2, articulo3])

    # Agregar el pedido al cliente
    cliente.agregar_pedido(pedido)



    # Imprimir detalles del cliente
    print(cliente)

    # Imprimir detalles del pedido
    print(pedido)

    # Imprimir detalles de los artículos
    for articulo in pedido.articulos:
        print(articulo)

if __name__ == "__main__":
    main()
