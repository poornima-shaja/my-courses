class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passenger = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passenger.append(name)
        return True
    def open_seats(self):
        return self.capacity - len(self.passenger)

flight = Flight(7)        
people = ["rm","jin","yoongi","jhope","jimin", "tae", "jungkook", "stalker"]
for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} in flight successfully")
    else:
        print(f"No avaliable seats for {person}")