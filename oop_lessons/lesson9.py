# class Calculator:
#     def add(self, *sonlar):
#         return sum([i**2 for i in sonlar if isinstance(i, int)]), [i.title() for i in sonlar if isinstance(i, str)]
#
#
# a = Calculator()
# print(a.add(2))
# print(a.add(2, 3))
# print(a.add('salom', 'django', 100, 123))







#
#
# class Shakl:
#     _name = "Shakl"
#     def get_area(self):
#         return 'area'
#
#     @property
#     def name(self):
#         return self._name
#
# class TogriTortburchak(Shakl):
#     _name = 'Togri Tortburchak'
#     def __init__(self, eni, boyi):
#         self.eni = eni
#         self.boyi = boyi
#
#     def get_area(self):
#         return self.eni*self.boyi
#
#
# class Kvadrat(Shakl):
#     _name = 'Kvadrat'
#     def __init__(self, tomon):
#         self.tomon = tomon
#
#     def get_area(self):
#         return self.tomon**2
#
#
# class Uchburchak(Shakl):
#     _name = 'Uchburchak'
#     def __init__(self, kated1, kated2):
#         self.kated1 = kated1
#         self.kated2 = kated2
#
#     def get_area(self):
#         return (self.kated2 * self.kated1)/2
#
#
# class Paralaliped(Shakl):
#     _name = 'Paralaliped'
#     def __init__(self, eni, boyi, balandlik):
#         self.eni = eni
#         self.boyi = boyi
#         self.balandlik = balandlik
#
#     def get_area(self):
#         return 2*(self.eni * self.boyi + self.eni * self.balandlik + self.balandlik * self.boyi)
#
#
# import math
# class Doira(Shakl):
#     _name = 'Doira'
#     def __init__(self, a, type_):
#         self.a = a
#         self.type_ = type_
#
#     def get_area(self):
#         if self.type_ == 'radius':
#             return math.pi * (self.a**2)
#         else:
#             return math.pi * (self.a/2)**2
#
# d1 = Doira(12, 'radius')
# t1 = TogriTortburchak(3, 7)
# k1 = Kvadrat(5)
# p1 = Paralaliped(2, 3, 8)
# # data = (t1, k1, p1)
# # for i in data:
# #     print(i.get_area())
#
# def get_result(shakl):
#     print(shakl.name, shakl.get_area())
#
#
# get_result(t1)
# get_result(p1)
# get_result(d1)




# class Xodim:
#     _name = "Xodim"
#
#     def __init__(self, name):
#         self.name_ = name
#
#     def maosh(self):
#         pass
#
#     @property
#     def name(self):
#         return {
#             "Lavozim": self._name,
#             "Ism": self.name_
#         }
#
# class Manager(Xodim):
#     _name = "Manager"
#     def __init__(self, name, day, narx):
#         Xodim.__init__(self, name)
#         self.day = day
#         self.narx = narx
#
#     def maosh(self):
#         x = self.narx * self.day
#         if x > 500:
#             x += 200
#         elif x > 400:
#             x += 100
#         return x
#
#
# class Developer(Xodim):
#     _name = 'Developer'
#     def __init__(self, name, projects, narx):
#         Xodim.__init__(self, name)
#         self.projects = projects
#         self.narx = narx
#
#     def maosh(self):
#         x = self.narx * self.projects
#         if x >= 900:
#             x += 500
#         elif x >= 600:
#             x += 100
#         return x
#
#
# m1 = Manager('Shaxriyor', 15, 25)
# m2 = Manager('Xayrullox', 20, 25)
# d1 = Developer("Asadbek", 4, 300)
# d2 = Developer('Baurjan', 2, 200)
# d3 = Developer('Mansurjon', 5, 200)
#
#
#
# def test(xodim):
#     print(xodim.name, xodim.maosh())
#
# test(d3)
# test(d1)
# test(d2)
# test(m1)
# test(m2)



# class Person:
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address
#
#
# class Address:
#     def __init__(self, vil, tum, mfy, uy, xonadon=None):
#         self.vil = vil
#         self.tum = tum
#         self.mfy = mfy
#         self.uy = uy
#         self.xonadon = xonadon
#
#     def get_address(self):
#         return self.vil, self.tum, self.mfy, self.uy, self.xonadon
#
#
# a1 = Address('Toshkent',  'Yunusobod',  'Vatanparvar',  4,  34)
#
# p1 = Person("Asadbek", 19, a1)
# print(p1.name)
# print(p1.age)
# print(p1.address.get_address())




