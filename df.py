import csv


# with open('config.csv', mode='r', newline='') as file:
#     writer = csv.writer(file)
    # writer.writerow(['name', 'age'])
    # writer.writerow(['Anvar', 12])
    # writer.writerow(['Anvar', 12])
    # writer.writerows([['Olim', 11],
    #                         ['Olim', 11],
    #                         ['Olim', 11],
    #                         ['Olim', 11]])
    # reader = csv.reader(file)
    # for row in reader:
    #     print(row[0])

# data = [
#         {'name': 'Olim', 'age': 11},
#         {'name': 'Olim', 'age': 11},
#         {'name': 'Olim', 'age': 11},
#         {'name': 'Olim', 'age': 11}
# ]
#
# with open('test.csv', mode='r', newline='') as file:
#     # fld = ('name', 'age')
#     # writer = csv.DictWriter(file, fieldnames=fld)
#     # writer.writeheader()
#     # writer.writerow({'name': 'Anvar', 'age': 12})
#     # writer.writerows(data)
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row['age'])

# import requests
# url = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"
# response = requests.get(url)
# data = response.json()
# for vlyt in data:
#     print(f'{vlyt}')










# try:
#     a = int(input(": "))
#     b = int(input(": "))
#     print(a/b)
# except ValueError as e:
#     print("Invalid input ", e)
# except ZeroDivisionError as e:
#     print("Division by zero is not allowed", e)
# print('finished')





# try:
#     file = open('n64.txt', 'r')
#     data = file.read()
# except Exception as e:
#     print("Error", e)
# else:
#     print(data)
# finally:
#     try:
#         file.close()
#     except Exception as e:
#         print("File close error", e)
#     print("dastur tugadi")



# try:
#     a = int(input(": "))
#     b = int(input(": "))
#     print(a/b)
# except ValueError as e:
#     print("Invalid input ", e)
# except ZeroDivisionError as e:
#     print("Division by zero is not allowed", e)
# print('finished')








# try:
#     a = int(input(": "))
#     b = int(input(": "))
#
#     if b == 0:
#         raise Exception("Boluvchi qiymati 0 ga teng bolmasligi kerak")
#
#     if a < 0 or b < 0:
#         raise Exception("Musbat son kiritilishi kerak")
#
#     print(a/b)
# except Exception as e:
#     print(e)











# class Person:
#     def __init__(self, name, age, country):
#         self.name = name
#         self.age = age
#         self.country = country
#
#     def get_full_info(self):
#         return f'{self.name}, {self.age}, {self.country}'
#
#
# # p1= Person('Asadbek', 20, 'Toshkent')
# # p2= Person('Xayrullox', 15, 'Xorazm')
#
#
# class Student(Person):
#     def __init__(self, name, age, country, grade, prof, group):
#         super().__init__(name, age, country)
#         self.grade = grade
#         self.prof = prof
#         self.group = group
#
#     def get_student_info(self):
#         return f'{self.name}, {self.age}, {self.country}, {self.grade}, {self.prof}, {self.group}'
#
# s1 = Student('Amirshoh', 20, 'Buxoro', 3, 'IT', 302)
# s2 = Student('Boyirjon', 20, 'Fargona', 2, 'CY', 205)
#
#
# print(s2.get_full_info())
# print(s2.get_student_info())


















































