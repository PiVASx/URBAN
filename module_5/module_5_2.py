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

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'


building_1 = House('ЖК Горский', 25)
building_2 = House('Домик в деревне', 2)

# __str__
print(building_1)
print(building_2)

# __len__
print(len(building_1))
print(len(building_2))