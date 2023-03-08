class Person:
    def __init__(self, _id, name):
        self.id = _id
        self.name = name
    
    def show_attr(self):
        print(f"{self.id}. {self.name}")