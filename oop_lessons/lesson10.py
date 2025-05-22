# import string
# from uuid import uuid4
#
#
# class Users:
#     _name = "Person"
#     num_ = []
#     def __init__(self, name, age, prof, id=uuid4()):
#             self._id = id
#             self.name = name
#             self.age = age
#             self.__prof = prof
#             self._gpa = 0
#             Users.num_.append((self.name, self.age, self.__prof))
#
#
#     def get_info_user(self):
#         return self.name
#
#     def get_prof(self):
#         return self.__prof, self._id
#
#     def __str__(self):
#         return self.name
#
#     def __lt__(self, other):
#         print('lt')
#         return self.age < other.age
#
#     def __gt__(self, other):
#         print('gt')
#         return self.age > other.age
#
#     def __eq__(self, other):
#         print('eq')
#         return self.age == other.age
#
#     def __call__(self, *args, **kwargs):
#         print(f'Salom {self.name}')
#
#     @classmethod
#     def get_name_cls(cls):
#         return cls._name
#
#     @classmethod
#     def get_num_obj(cls):
#         return len(cls.num_)
#
#     @classmethod
#     def add_(cls, data):
#         name, age, prog = data.split('-')
#         # cls.num_.append((name, age, prog))
#         return cls(name, age, prog)
#
#     # @classmethod
#     # def get_users(cls):
#     #     return cls.num_
#
#
#     @staticmethod
#     def test(ball):
#         return sum(ball)/len(ball)
#
#     @property
#     def gpa(self):
#         return self._gpa
#
#     @gpa.setter
#     def gpa(self, ballar):
#         self._gpa = self.test(ballar)
#
#
# u1 = Users('Xayrullox', 15, 'Python')
# u2 = Users("Javohir", 18, 'Java')
# u3 = Users("Javohir", 18, 'Java')
# # print(Users.get_name_cls())
# # print(Users.num_)
# # /u4 = Users.add_('Salohiddin-18-c++')
# # print(Users.num_)
# # print(u1.test(4, 5, 3, 2, 0))
# u1.gpa = (1, 3, 5)
# print(u1.gpa)
# # print(u1.__sizeof__())
# # print(u1.__doc__)
# # print(type(u1))
# # x = {34, 89}
# # print(x)
# # print(isinstance(x, set))
#
#
# # class Number:
# #     def __init__(self, x): self.x = x
# #
# #     def __add__(self, other): return self.x + other.x
# #
# #     def __sub__(self, oter): return self.x - oter.x
# #
# #     def __mul__(self, oter): return self.x * oter.x
# #
# #     def __len__(self): return len(self.x)
# #
# #
# # n1 = Number([2, 8, 9, 0])
# # print(len(n1))
# # n2 = Number(13)
# # print(n1 - n2)
# # print(n1 + n2)
# # print(n1 * n2)
#
# #
# # class Mylist:
# #     def __init__(self): self.data = {}
# #
# #     def __getitem__(self, item):
# #         return self.data[item]
# #
# #     def __setitem__(self, key, value):
# #         self.data[key] = value
# #
# #     def __del__(self, key):
# #         del self.data
# #
# #
# # m1 = Mylist()
# # m1.data['1'] = 'dadqwd'
# # m1.data['2'] = 'dadqwd'
# # m1.data['3'] = 'dadqwd'
# # m1.data['4'] = 'dadqwd'
# # m1.data['5'] = 'dadqwd'
# # del m1
# # print(m1.data)
#
#
#
#
#
# class Cars:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price
#
#     @classmethod
#     def from_string(cls, data):
#         brand, model, price = data.split('-')
#         return cls(brand, model, int(price))
#
#     @staticmethod
#     def apply_discount(price):
#         return price * 0.9
#
#     def get_info(self):
#         return self.brand
#
#
# import math
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     @staticmethod
#     def calculate_area(radius):
#         return math.pi * radius**2
#
#
# circle = Circle(7)
# print(circle.calculate_area(5))


# 6
#
#
# import uuid
# class Product:
#   def __init__(self, name, price):
#     self.name = name
#     self.price = price
#
#   def __str__(self):
#     return f"product: {self.name.title()} -- £{self.price}"
#
# class Cart:
#   def __init__(self):
#     self.products.csv = []
#
#
#   def add_product(self, product):
#     self.products.csv.append(product)
#
#   def remove_product(self, product):
#     if product in self.products.csv:
#       self.products.csv.remove(product)
#
#   @property
#   def total_price(self):
#     return sum(product.price for product in self.products.csv)
#
#
# class User:
#   def __init__(self, name, cart):
#     self.name = name
#     self.cart = cart
#     self.id = self.generate_user_id()
#
#   @staticmethod
#   def generate_user_id():
#     return str(uuid.uuid4())
#
#   def __str__(self):
#     return f"{self.name} : {self.user_id}"
#
#
# class Store:
#   def __init__(self):
#     self.users = []
#
#   def add_users(self, user):
#     self.users.append(user)
#
#   def remove_users(self, user):
#     self.users.remove(user)
#
#   def search_by_id(self, id):
#     for user in self.users:
#       if user.id == id:
#         return [product.name for product in user.cart.products.csv], sum([product.price for product in user.cart.products.csv])
#
#
# cart1 = Cart()
# user1 = User("Rustamjon", cart1)
# products1 = [Product("Comb", 3), Product("Notebooks", 5), Product("Pen", 2)]
# for product in products1:
#   cart1.add_product(product)
#
# # print(cart1.total_price)
# # print(user1.id)
#
# cart2 = Cart()
# user2 = User("Asadbek", cart2)
# products2 = [Product("Comb", 5), Product("Notebooks", 5), Product("Pen", 2)]
# for product in products2:
#   cart2.add_product(product)
#
# # print(cart2.total_price)
# # print(user2.id)
#
# store = Store()
# store.add_users(user1)
# store.add_users(user2)
# print(store.search_by_id(user1.id))


# class Book:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
#
#     def __str__(self):
#         return f"{self.title} by {self.author}, published in {self.year}"
#
#
# class Reader:
#     def __init__(self, name, id, borrowed_books=None):
#         if borrowed_books is None:
#             borrowed_books = []
#         self.name = name
#         self.id = id
#         self.borrowed_books = borrowed_books
#         self.conf = False
#
#     def borrow_book(self, book):
#         self.borrowed_books.append(book)
#         return self.borrowed_books
#
#     @property
#     def borrowed_count(self):
#         return len(self.borrowed_books)
#
#
# class Library:
#     # count_book = 0
#     def __init__(self):
#         self.books = []
#         # Library.count_book += 1
#
#     def list_books(self):
#         return [i.title for i in self.books]
#
#     def add_book(self, book):
#         self.books.append(book)
#
#     def remove_book(self, title):
#         self.books = [i for i in self.books if i.title != title]
#
#     @classmethod
#     def total_books(cls):
#         return len(cls.book)
#
#
# b1 = Book("1984", "George Orwell", 1949)
# b2 = Book("198432", "George Orwell", 1949)
# print(b1)
# r1 = Reader("user1", 101)
# l1 = Library()
#
# l1.add_book(b1)
# l1.add_book(b2)
# print(l1.list_books())
# for i in r1.borrow_book(b1):
#     print(i)
# print(r1.borrowed_count)


# class Dish:
#     def __init__(self, name, price, time_to_prepare):
#         self.name = name
#         self.price = float(price)
#         self.time_to_prepare = float(time_to_prepare)
#
#     @property
#     def info(self):
#         return f"{self.name} - ${self.price:}, tayyorlanish vaqti: {self.time_to_prepare} daqiqa"
#
#
# class Menu:
#     def __init__(self):
#         self.dishes = []
#
#     def add_dish(self, dish):
#         self.dishes.append(dish)
#
#     def remove_dish(self, dish):
#         if dish in self.dishes:
#             self.dishes.remove(dish)
#
#
# class Order:
#     def __init__(self, customer):
#         self.dishes = []
#         self.customer = customer
#
#     def calculate_total(self):
#         return sum(dish.price for dish in self.dishes)
#
#
# class Customer:
#     def __init__(self, name):
#         if not self.is_valid_name(name):
#             raise ValueError("Noto‘g‘ri ism formati!")
#         self.name = name
#
#     @staticmethod
#     def is_valid_name(name):
#         return isinstance(name, str) and len(name.strip()) > 0 and name == name.capitalize()
#
#
#
# dish1 = Dish("Pizza", 12, 20)
# dish2 = Dish("Mastava", 9, 15)
#
# menu = Menu()
# menu.add_dish(dish1)
# menu.add_dish(dish2)
#
# customer = Customer("Malika")
# order = Order([dish1, dish2], customer)
#
# print(dish1.info)
# print(dish2.info)
# print(f"Buyurtma summasi: ${order.calculate_total()}")


# 9 - masala


# class Player:
#
#     def __init__(self, name: str, age: int, status: bool = True):
#         self.name: str = name
#         self.age: int = age
#         self.status: bool = status
#
#     def checker(self):
#         if self.age > 35:
#             self.name = False
#
#
# class Footballer(Player):
#
#     def __init__(self, name: str, age: int, position: str, status: bool = True, ):
#         super().__init__(name, age, status)
#         self.position: str = position
#
#     def before_add(self):
#         if self.status == True:
#             return f"{self.name} {self.age} {self.position} {self.status}"
#
#
# class Basketballer(Player):
#
#     def __init__(self, name: str, age: int, position: str, status: bool = True, ):
#         super().__init__(name, age, status)
#         self.position: str = position
#
#     def before_add(self):
#         if self.status == True:
#             return f"{self.name} {self.age} {self.position} {self.status}"
#
#
# class Volleyballer(Player):
#     def __init__(self, name: str, age: int, position: str, status: bool = True, ):
#         super().__init__(name, age, status)
#         self.position: str = position
#
#     def before_add(self):
#         if self.status == True:
#             return f"{self.name} {self.age} {self.position} {self.status}"
#
#
# class Team:
#     footballers = []
#     backetballer = []
#     voleyboller = []
#
#
# # 4 - masala
# class Account:
#     def __init__(self, owner: str, balance: float = 0):
#         self.owner: str = owner
#         self.balance: float = balance
#
#     def deposit(self, pul):
#         self.balance += pul
#         return (f"{self.owner}ning puliga {pul} pul qo'shildi\n"
#                 f"Jami account balance {self.balance} bo'ladi")
#
#     def withdraw(self, pul):
#         if self.balance >= pul:
#             self.balance -= pul
#             return f"{pul} pul yechildi. Yangi balans: {self.balance}"
#         else:
#             return (f"Hurmatli {self.owner}, hisobingizda {pul} yechish uchun yetarli mablag' yo'q\n"
#                     f"Hozirgi balance: {self.balance}")
#
#     @property
#     def balance_info(self):
#         return f"Hurmatli {self.owner}, balansingiz: {self.balance}"
#
#
# class Bank:
#     accounts = []
#
#     @classmethod
#     def add_account(cls, account: Account):
#         cls.accounts.append(account)
#
#     @staticmethod
#     def give_info():
#         for acc in Bank.accounts:
#             print(acc.balance_info)
#
#     @staticmethod
#     def total_acccount():
#         return len(Bank.accounts)
#
#
# acc1 = Account("Vali")
# acc2 = Account("Karim")
# acc3 = Account("Ali")
#
# acc1.deposit(500_000)
# acc2.deposit(1000_000)
# acc3.deposit(100_000)
# # Accountlarni bankka qo‘shish
# Bank.add_account(acc1)
# Bank.add_account(acc2)
# Bank.add_account(acc3)
#
# Bank.give_info()
# print(Bank.total_acccount())


# 5-loyha
class HayvonBogi:
    def __init__(self, name, lokatin):
        self.name = name
        self.lokation = lokatin
        self.hayvonlar = []

    def get_info(self):
        return self.name, self.lokation

    def add_hayvon(self, hayvon):
        self.hayvonlar.append(hayvon)

    def print_hayvonlar(self):
        return [i.get_info() for i in self.hayvonlar]

    def remove_hayvon(self, hayvon_nomi):
        for i in self.hayvonlar:
            # print(len(i.get_info().split()[2].split(':')[-1]))
            if i.get_info().split()[2].split(':')[-1] == hayvon_nomi:
                self.hayvonlar.remove(i)
                return True
        else:
            return "Bizda bunday hayvon mavjud emas!"


class Hayvonlar:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"hayvon nomi {self.name}  hayvon yoshi {self.age}"

    def ovoz_chiqar(self):
        return ""


class Sher(Hayvonlar):
    def __init__(self, name, age):
        Hayvonlar.__init__(self, name, age)

    def ovoz_chiqar(self):
        return "Sherni auazi"


class FIl(Hayvonlar):
    def __init__(self, name, age):
        Hayvonlar.__init__(self, name, age)

    def ovoz_chiqar(self):
        return "Filni avozi"


class Maymun(Hayvonlar):
    def __init__(self, name, age):
        Hayvonlar.__init__(self, name, age)

    def ovoz_chiqar(self):
        return "Maymuni auazi"


m = HayvonBogi("Hayvonlar olami", "Toshkent")
sher = Sher("Sher:simba", 12)
fil = FIl("FIL:Mango", 23)
maymun = Maymun("Maymun:Lago", 23)
m.add_hayvon(sher)
m.add_hayvon(maymun)
m.add_hayvon(fil)
while True:
    a = input(
        "1-Hayvonat bogidagi hayvonlar royhati | 2-hayvonat bogidagi hayvonlar sonini korish | 3-hayvonat bogiga hayvon qoshish | 4-hayvonat bogidan hayvoni chiqarish  | 0 - chiqish---->")
    if a == "1":
        print(m.print_hayvonlar())
    elif a == "2":
        print(f"bizning hayvonot bogimizda {len(m.print_hayvonlar())} ta hayvon bor")
    elif a == "3":
        name_h = input("hayvon nomini kiriting:")
        age_h = int(input("hayvon yoshini kiriting:"))
        n3 = Hayvonlar(name_h, age_h)
        print(m.add_hayvon(n3))
    elif a == "4":
        n = input("Hayvon nomini kiritng:")
        m.remove_hayvon(n)
    elif a == "0":
        print("Hayr salomot boling!")
        break
    else:
        print("Notogri malumot kiritingiz qayta urinib koring :)")
