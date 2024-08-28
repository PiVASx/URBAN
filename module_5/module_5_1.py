class House:
    def __init__(self, name, number):
        self.name = name
        self.number_of_floors = number

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for i in range(1, new_floor+1):
                print(i)
        else:
            print("Такого этажа не существует")


building_1 = House('ЖК Горский', 25)
building_2 = House('Домик в деревне', 2)
building_1.go_to(6)
building_2.go_to(5)
