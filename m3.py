# import random
# data = set()
# n = 20
# for i in range(n):
#     key = random.randint(-50, 51)
#     data.add(key)
# print(data)


# d = {"a": {"b": {"c": 100}}}

# def test_(lst):
#     for i in lst:
#         if isinstance(i, dict):
#             test_(list(i.values()))
#         else:
#             print(i)


d = {"a": {"b": {"c": 100}}}
d1 = d
# kalit = ["c", "b", 'a']
# for k in kalit:
#     if k in d1:
#         d1 = d1[k]
#     else:
#         print('not found')
#         break
# print(d1)





# scores = [(1, 78), (2, 95), (3, 88), (4, 65)]
# dct = {i[0]: i[1] for i in scores}
# print(sorted(dct.items(), key=lambda x: x[1]))



class Computer:
    def __init__(self, brand, model, price, year, country, size):
        self.brand = brand
        self.model = model
        self.price = price
        self.year = year
        self.country = country
        self.size = size
        self._ghz = 1

    def _get_full_info(self):
        return f'Brand: {self.brand}, Model: {self.model}, Price: {self.price}, Year: {self.year}, Country: {self.country}, Size: {self.size} inches, Age: {self.__age()}'

    def __age(self):
        return 2025 - self.year

    @property
    def ghz(self):
        return self._ghz

    @ghz.setter
    def ghz(self, x):
        if x < 1:
            print('Siz xato ghz kiritdingiz')
        else:
            self._ghz = x



comp1 = Computer('HP', 'Pavilion', 500, 2021, 'China', 15.6)
# print(comp1.get_full_info())
# print(comp1.age())
# print(comp1._get_full_info())
comp1.ghz = 0.5
print(comp1.ghz)
# print(comp1.get_ghz())


class Category:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self._dollor = 12900

    @property
    def dollor(self):
        return self.price / self._dollor

    @dollor.setter
    def dollor(self, vallue):
        if vallue <= 12000 or vallue >= 14000:
            print("Xato malumot kiritdizgiz")
        else:
            self._dollor = vallue

c2 = Category('Computer', 12900000)
c2.dollor = 13500 #98
print(c2.dollor)#100






