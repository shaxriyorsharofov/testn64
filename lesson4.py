# import csv

# data = [
#     [1, "Alisher", 15, "A"],
#     [2, "Madina", 14, "B"],
#     [3, "Islom", 16, "A"],
#     [4, "Sarvar", 15, "C"],
#     [5, "Dilnoza", 14, "B"]
# ]
#
# with open('students.csv', mode='w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['ID', 'Name', 'Age', 'Grade'])
#     writer.writerows(data)

# with open('students.csv', mode='r', newline='') as file:
#     writer = csv.reader(file)
#     for i in writer:
#         if i[2].isdigit():
#             if int(i[2]) > 15:
#                 with open('group_1.csv', mode='a', newline='') as group_1_file:
#                     writer = csv.writer(group_1_file)
#                     writer.writerow(i)
#             else:
#                 with open('group_2.csv', mode='a', newline='') as group_2_file:
#                     writer = csv.writer(group_2_file)
#                     writer.writerow(i)



# class Students:
#     def __init__(self, name, age, country):
#         self.name = name
#         self.age = age
#         self.country = country
#         self.level = 1
#
#     def set_level(self, a=1):
#         self.level = self.level + 1 if a == 1 else a
#
#     def get_level(self):
#         return self.level
#
#     def set_age(self, a=1):
#        if a == 1:
#            self.age += 1
#        else:
#            self.age = a
#
#     def get_info(self):
#         return f"Name: {self.name}, age:{self.age}, country:{self.country}, level:{self.level}"
#
#
# class Group:
#     def __init__(self, name, prof):
#         self.name = name
#         self.prof = prof
#         self.students = []
#
#     def get_info(self):
#         return self.name, self.prof
#
#     def add_students(self, student):
#         self.students.append(student)
#
#     def get_students(self):
#         return [student.get_info() for student in self.students]
#
#
#
#     def delete_students(self, student_name):
#         for student in self.students:
#             user = student.get_info().split(',')[0].split()[1]
#             if user == student_name:
#                 self.students.remove(student)
#         else:
#             print("Siz xato malumot kiritdingiz!")
#
#     def all_students(self):
#         return len(self.students)
#
# n64 = Group('Standart Python Django N64', 'Python Django')
#
#
# s1 = Students('Asadbek', 20, 'Toshkent')
# s2 = Students('Xayrullox', 15, 'Toshkent')
# s3 = Students('Mansurjon', 18, 'Buxoro')
# s4 = Students('Amirshox', 20, 'Buxoro')
# s5 = Students('Baurjan', 18, 'Toshkent')
#
# n64.add_students(s1)
# n64.add_students(s2)
# n64.add_students(s3)
# n64.add_students(s4)
# n64.add_students(s5)
#
#
# n64.delete_students('Xayrulloxd')

# print(n64.all_students())
# print(n64.get_students())







class Dori:
    def __init__(self, nomi, narxi, country, soni = 0):
        self.nomi = nomi
        self.narxi = narxi
        self.country = country
        self.soni = soni

    def get_info(self):
        return f"Dori nomi: {self.nomi}, narxi: {self.narxi}, davlati:{self.country}, soni:{self.soni}"

class Dorixona:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.dorilar = 'dorilar.txt'
        self.balanse = 0

    def get_dorixona_info(self):
        return self.name, self.location

    def add_dorilar(self, dori_nomi, dori_soni):
        for dori in self.dorilar:
            if dori.nomi == dori_nomi:
                dori.soni += dori_soni
                return 'Dori qoshildi'
        else:
            return 'Siz xato malumot kiritdingiz'

    def add_new_dorilar(self, dori):
        with open(f"{self.dorilar}", 'a') as dori_file:

            dori_file.write(dori)


    def get_dorilar(self):
        i = 1
        for dori in self.dorilar:
            print(f"{i}.{dori.get_info()}")
            i += 1

    def del_info(self, dori_nomi, soni):
        for dori in self.dorilar:
            if dori.nomi == dori_nomi:
                if dori.soni == 0:
                    return 'Bizda bu doridan qolmagan'
                elif dori.soni >= soni:
                    dori.soni -= soni
                    self.balanse += (soni * dori.narxi)
                    return f"{dori_nomi} xarid qilindi.({dori.soni} ta qoldi)"
                else:
                    return f"{dori.soni} ta mavjud bizda"
        else:
            return 'Bizda bunday dori mavjud emas '

    def all_dorilar(self):
        return len(self.dorilar)

    def get_balanse(self):
        return self.balanse


dorixona = Dorixona('Aybalit', 'Toshkent')

d1 = Dori('trimol', 2000, 'UZB', 10)
d2 = Dori('qupen', 5000, 'Indiya', 8)
d3 = Dori('Analgin', 30000, 'Amerika', 5)
d4 = Dori('ACC', 3000, 'Amerika', 50)

dorixona.add_new_dorilar(d1)
dorixona.add_new_dorilar(d2)
dorixona.add_new_dorilar(Dori(dori_nomi, dori_narxi, dori_country, dori_soni))

while True:
    a = input('1-dorilar|2-dorixona malumotlari|3-dori olish|4-dori qoshish|0-chiqish--->')
    if a == '1':
        dorixona.get_dorilar()
    elif a == '2':
        print(dorixona.get_dorixona_info())
    elif a == '3':
        dori_nomi = input('Dori nomi:')
        dori_soni = int(input('Dori soni:'))
        dorixona.del_info(dori_nomi, dori_soni)
        print('Summa: ', dorixona.get_balanse())
    elif a == '0':
        break
    elif a == '4':
        dori_nomi = input('Dori nomi:')
        dori_soni = int(input('Dori soni:'))
        print(dorixona.add_dorilar(dori_nomi, dori_soni))
    else:
        print("Siz adashdingiz, qaytadan urinib koring")
# print(dorixona.del_info('trimol', 8))
# print(dorixona.del_info('Analgin', 1))





























