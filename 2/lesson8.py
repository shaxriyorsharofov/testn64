# a = [10, 20, 11, 26, 40, 50, 22] #10, 22, 20, 50, 11, 40, 26
# b = []
# n = len(a)
# x = len(a)
# for i in range(n):
#     d = -1**i
#     if d >= 0:
#         b.append(a[i])
#     else:
#         b.append(a[x-i])
# print(b)


# a = [10, 20, 11, 26, 40, 50, 22] #10, 22, 20, 50, 11, 40, 26
# def main(n, k, l):
#     return sum(n[k:l+1])


# a = 'salom  python django dunyo'
# result = min(a.split()[::-1], key=len)
# print(result)



# a = 'minimum uzunlikdagi kiyik'
# for i in a.split():
#     print(i.replace(i[0], '.').replace('.', i[0], 1))
# print(' '.join([i.replace(i[0], '.').replace('.', i[0], 1) for i in a.split()]))


# l = [0, 1]
# for i in range(10):
#     a = l[i] + l[i + 1]
#     l.append(a)
# print(l)

# a = 11
# s = 0
# for i in range(1, a+1):
#     if a % i == 0:
#         s += i
# print(s)
#
# if s == 2:
#     print('tub')


from random import randint
from faker import Faker
from lesson10 import *

# a = [10, 20, 11, 26, 40, 50, 220]
# print(randint(0, 20))
# fake = Faker()
# for i in range(100):
#     print(f"Name:{fake.name()} Address: {fake.address()} Year: {fake.year()} Month: {fake.month()}")


# import cowsay
# cowsay.cow("Pythonni o'rgan")


# from lesson10 import test_ as t
# print(t([10, 20, 11, 26, 40, 50, 220]))
# print(__file__)




