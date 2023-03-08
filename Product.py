class Product:
    def __init__(self, _id, name, quantity, price):
        self.id = _id
        self.name = name
        self.quantity = quantity
        self.price = price
    def show_attr(self):
        print(f"\t- Nombre: {self.name}\n\t- Cantidad: {self.quantity}\n\t- Precio unitario: ${self.price}")