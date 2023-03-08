from Person import Person

class Guest(Person):
    def __init__(self, _id, name, seat, allergies, confirmed):
        self.seat = seat
        self.allergies = allergies
        self.confirmed = confirmed
        super().__init__(_id, name)
    
    def show_attr(self):
        print(f"{self.id}. {self.name}\n- Asiento: {self.seat}\n- Alergias: {' | '.join(self.allergies) if len(self.allergies) > 0 else '-'}\n- Confirmado: {'✅' if self.confirmed else '❌'}")