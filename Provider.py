class Provider:
    def __init__(self, _id, name, products):
        self.id = _id
        self.name = name
        self.products = products
    
    def show_attr(self):
        print(f"  * {self.name}")
        print("    Productos:")
        for p in self.products:
            p.show_attr()
            print()