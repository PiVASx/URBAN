class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        cont = file.read()
        file.close()
        return cont

    def add(self, *products: Product):
        file = open(self.__file_name, 'r+')
        cont = file.read()

        for prod in products:
            if str(prod) not in cont:
                file.write(str(prod) + '\n')
            else:
                print(f'{str(prod)} уже есть в магазине')

        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__
print()

s1.add(p1, p2, p3)
print()
print(s1.get_products())