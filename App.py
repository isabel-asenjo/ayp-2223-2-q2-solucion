from Guest import Guest
from Product import Product
from Provider import Provider
from StaffMember import StaffMember

class App:
    old_db = {
            "Guests":
        [
            { "id": 1, "name": "Lyla Jenkins", "seat": "1A", "allergies": ["Shrimp"], "confirmed": False },
            { "id": 2, "name": "Harvey Wyatt", "seat": "1B", "allergies": [], "confirmed": False },
            { "id": 3, "name": "Logan Clay", "seat": "1C", "allergies": [], "confirmed": False },
            { "id": 4, "name": "Cormac Gregory", "seat": "1D", "allergies": ["Lavender", "Cake"], "confirmed": False },
            { "id": 5, "name": "Matthew Maddox", "seat": "1E", "allergies": [], "confirmed": False },
            { "id": 6, "name": "Clarence Delacruz", "seat": "2A", "allergies": ["Shrimp"], "confirmed": False },
            { "id": 7, "name": "Halima Parsons", "seat": "2B", "allergies": [], "confirmed": False },
            { "id": 8, "name": "Connie Lewis", "seat": "2C", "allergies": ["Cake"], "confirmed": False },
            { "id": 9, "name": "Cassie Marks", "seat": "2D", "allergies": ["Lavender"], "confirmed": False },
            { "id": 10, "name": "Esha Lane", "seat": "2E", "allergies": ["Shrimp"], "confirmed": False },
        ],
    
        "Staff":
        [
            { "id": 1, "name": "Bessie Daniel", "salary": 1000.00 },
            { "id": 2, "name": "Roosevelt Beltran", "salary": 1000.00 },
            { "id": 3, "name": "Luisa Todd", "salary": 1000.00 },
            { "id": 4, "name": "Scarlett Bolton", "salary": 1200.00 },
            { "id": 5, "name": "Maryam Hines", "salary": 1200.00 },
            { "id": 6, "name": "Laila Stanley", "salary": 2150.00 },
            { "id": 7, "name": "Theodore Salinas", "salary": 2150.00 },
            { "id": 8, "name": "Michael Contreras", "salary": 3000.00 },
            { "id": 9, "name": "Shane Whitney", "salary": 3000.00 },
        ],
    
        "Providers":
        [
            { "id": 1, "name": "The Maroon Carnation C.A.", "products": [1] },
            { "id": 2, "name": "Este's Enchanting Catering", "products": [2, 3, 4] },
            { "id": 3, "name": "Mirrorball Productions", "products": [5, 6]},
        ],
    
        "Products":
        [
            { "id": 1, "name": "Lavender", "quantity": 30, "price": 12.20 },
            { "id": 2, "name": "Shrimp", "quantity": 100, "price": 1.50 },
            { "id": 3, "name": "Pasta", "quantity": 100, "price": 5.30 },
            { "id": 4, "name": "Cake", "quantity": 1, "price": 150.00 },
            { "id": 5, "name": "DJ", "quantity": 1, "price": 3000.00 },
            { "id": 6, "name": "Musical guest", "quantity": 2, "price": 12000.00 },
        ],
    }

    def __init__(self):
        # no tengo lista de productos porque los productos los voy a guardar dentro de cada proveedor
        self.providers = []
        self.staff_members = []
        self.guests = []

    def load_data(self):
        # esta parte está hecha con list comprehensions pero se puede hacer con for loops normales
        
        self.guests = [Guest(g['id'], g['name'], g['seat'], g['allergies'], g['confirmed']) for g in self.old_db['Guests']]
        
        self.staff_members = [StaffMember(s['id'], s['name'], s['salary']) for s in self.old_db['Staff']]
        
        products_temp = [Product(p['id'], p['name'], p['quantity'], p['price']) for p in self.old_db['Products']] # primero creo los productos para guardarlos dentro de los providers
        self.providers = [Provider(prov['id'], prov['name'], [p for p in products_temp if p.id in prov['products']]) for prov in self.old_db['Providers']]


    def guest_list(self):
        print("INVITADOS 🤵")
        for guest in self.guests:
            guest.show_attr()
            print()


    def providers_list(self):
        print("PROVEEDORES 📦")
        for prov in self.providers:
            prov.show_attr()
            print()


    def confirm_attendance(self):
        self.guest_list() # se muestra la lista de invitados

        guest_id = input("Ingrese el id del invitado que confirmará su asistencia: ") # se pide el id

        # si el id no existe, se notifica y no se hace nada más
        if not guest_id.isnumeric() or int(guest_id) not in map(lambda g: g.id, self.guests):
            print("No existe un invitado con este id.")
        else: # si se consigue el id, se busca al invitado que tenga ese id y se cambia el valor de confirmed
            for g in self.guests:
                if g.id == int(guest_id):
                    g.confirmed = True
                    break
            print("Asistencia confirmada con éxito!")


    def stats(self):
        print("ESTADÍSTICAS 📊")

        allergies = []
        for g in self.guests:
            allergies += g.allergies
        print("- Productos a los que los invitados son alérgicos:", ", ".join(list(set(allergies))))

        total = 0
        # sumo los salarios de los empleados
        for sm in self.staff_members:
            total += sm.salary

        # sumo los precios de los productos multiplicados por la cantidad solicitada
        for prov in self.providers:
            for prod in prov.products:
                total += prod.price * prod.quantity

        print("- Costo total de la boda: $", total)


    def start(self):
        # transformo la info inicial en objetos
        self.load_data()

        while True:
            print("🎊 AGENCIA DE PLANIFICACIÓN DE BODAS - BODA #2320 🎊")
            print("1. Ver lista de invitados\n2. Ver proveedores\n3. Confirmar asistencia de invitado\n4. Estadísticas\n5. Salir")
            
            x = input("> ")
            
            print()

            if x == "1":
                self.guest_list()
            elif x == "2":
                self.providers_list()
            elif x == "3":
                self.confirm_attendance()
            elif x == "4":
                self.stats()
            elif x == "5": break
            else: print("Ingreso inválido. Intente otra vez.")
            
            print()