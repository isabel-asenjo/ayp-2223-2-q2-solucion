from Person import Person

class StaffMember(Person):
    def __init__(self, _id, name, salary):
        self.salary = salary
        super().__init__(_id, name)
    
    def show_attr(self):
        print(f"  - Nombre: {self.name}\n  - Salario: {self.salary}")