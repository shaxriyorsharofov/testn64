# a = {"Prezident": "Rashid", "Vazir": "Sharofat", "Parlament": "Behruzbek", "Senat": "Anorjon", "Xalq": "Miraziz"}
# try:
#     key_ = input(": ")
#     data = a[key_]
# except Exception as e:
#     print("Bunday kalit yoq", e)
# else:
#     print(data)


# import math
# try:
#     key_ = int(input(": "))
#     data = math.sqrt(key_)
# except Exception as e:
#     print("Musbat son kiriting!", e)
# else:
#     print(data)

# try:
#     key_ = int(input(": "))
#     data = math.sqrt(key_)
# except Exception as e:
#     print("Musbat son kiriting!", e)
# else:
#     print(data)

# try:
#     key_ = int(input(": "))
#     data = math.sqrt(key_)
# except Exception as e:
#     print("Musbat son kiriting!", e)
# else:
#     print(data)
    
    
    
# try:
#     key_ = input(": ")
#     __import__ (key_)
# except Exception as e:
#     print("BUnday module yoq", e)
# else:
#     print(True)


# class Company:
#     def __init__(self, name_com, year_com, location_com):
#         self.name_com = name_com
#         self.year_com = year_com
#         self.location_com = location_com
#
#
#     def get_company(self):
#         return self.name_com, self.year_com, self.location_com
#
#
# class Person:
#     def __init__(self, name, age, location):
#         self.name = name
#         self.age = age
#         self.location = location
#
#     def get_person(self):
#         return self.name, self.age, self.location
#
#
# class Employee(Company, Person):
#     def __init__(self, name, age, location, name_com, year_com, location_com, prof, level, salary=0):
#         # super(Company, self).__init__(name_com, location_com, year_com)
#         # super(Person, self).__init__(name, age, location, )
#         Person.__init__(self, name, age, location)
#         Company.__init__(self, name_com, year_com, location_com)
#         self.prof = prof
#         self.level = level
#         self.salary = salary
#
#
#     def get_info(self):
#         return self.prof, self.level, self.salary
#
# e1 = Employee('Xayrulloh', 15, 'Tashkent', 'Epam', 2018, 'Tashkent',\
#               'Python developer', 'Junior', 400)
# print(e1.get_info())
# print(e1.get_person())
# print(e1.get_company())






# class Person:
#     def __init__(self, name, age, location):
#         self.name = name
#         self.age = age
#         self.location = location
#
#     def get_person(self):
#         return self.name, self.age, self.location
#
#
# class Student(Person):
#     def __init__(self, name, age, location, prof, university):
#         Person.__init__(self, name, age, location)
#         self.prof = prof
#         self.university = university
#
#     def get_student(self):
#         return self.university, self.prof
#
#
# class Employee(Student):
#     def __init__(self, name, age, location, prof, university, level, salary=0):
#         Student.__init__(self, name, age, location, prof, university,)
#         self.level = level
#         self.salary = salary
#
#     def get_info(self):
#         return self.level, self.salary
#
#
# e1 = Employee('Baurjan', 18, 'Tashkent', 'IT', 'TDIU', 'Senior', 2500)
# print(e1.get_info())
# print(e1.get_person())
# print(e1.get_student())



# class Cars:
#     def __init__(self, make, model, year, color):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.color = color
#
#     def get_info_car(self):
#         return self.make, self.model, self.year, self.color
#
#
# class OilCars(Cars):
#     def __init__(self, make, model, year, color, oil_type, km_100):
#         Cars.__init__(self, make, model, year, color)
#         self.oil_type =oil_type
#         self.km_100 = km_100
#
#     def get_oil_car(self):
#         return self.km_100, self.oil_type
#
#
# class ElectrCars(Cars):
#     def __init__(self, make, model, year, color, batary_km, zaryadlash_tezligi):
#         Cars.__init__(self, make, model, year, color)
#         self.zaryadlash_tezligi = zaryadlash_tezligi
#         self.batary_km = batary_km
#
#     def get_elect_car(self):
#         return self.zaryadlash_tezligi, self.batary_km
#
#
# class HybridCars(OilCars, ElectrCars):
#     def __init__(self, make, model, year, color, oil_type, km_100, batary_km, zaryadlash_tezligi, x):
#         OilCars.__init__(self, make, model, year, color, oil_type, km_100)
#         ElectrCars.__init__(self, make, model, year, color, batary_km, zaryadlash_tezligi)
#         self.x = x
#
#
#     def get_info(self):
#         return self.km_100, self.zaryadlash_tezligi, self.oil_type, self.batary_km
#
#
#
# h1 = HybridCars('BYD', 'Chazor', 2024, 'black', 92, 4, 400, 1.5, 5)
# print(h1.get_info())
# print(h1.get_oil_car())
# print(h1.get_elect_car())
# print(h1.get_info_car())
# print(h1.x)



# from lesson7 import Ishchi, Users
#
# i1 = Ishchi('Javohir', 19, 'Java', 200, 12900, 20)
# print(i1._Ishchi__dollor)
# # print(i1._id)
# u1 = Users('Xayrullox', 15, 'Python')
# print(u1._Users__prof)