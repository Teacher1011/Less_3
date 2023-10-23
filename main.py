class Human:
    def __init__(self, name="Human"):
        self.name = name

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passengers(self, *args):
        for passenger in args:
            self.passengers.append(passenger)

    def print_passengers_names(self):
        if self.passengers != []:
            print(f"Імена пасажирів {self.brand}:")
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print(f"Пасажирів в {self.brand} немає")

car = Auto("Мерседес")
for i in range(4):
    p1 = Human(input("Введіть ім'я пасажира"))
    car.add_passengers(p1)
#p2 = Human("Кіра")

car.print_passengers_names()


