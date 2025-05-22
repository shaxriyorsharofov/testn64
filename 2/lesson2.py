# def task(n, m, k):
#     return f"Musbatlar soni:{((1 if n > 0 else 0) + (1 if m > 0 else 0) + (1 if k > 0 else 0))}, manfiylar soni:\
# {((1 if n < 0 else 0) + (1 if m < 0 else 0) + (1 if k < 0 else 0))}"
#
# print(task(2, -2, 9))


# def teskari(a, b):
#     a, b = a if a < b else b, a if a > b else b
#     return f"Teskari a:{a}, b:{b}"
#
# print(teskari(10, 5))

# a = 3
# b = 4
# d = 7
# c = a
# a = b
# b = c
# print(f"a: {a}, b: {b}")


# def task(n):
#     s = 1
#     while n > 0:
#         s *= n
#         n -= 2
#     return s
#
# print(task(6))


# def task(n):
#     i = 1
#     s = 0
#     while n >= i:
#         i *= 3
#         s += 1
#     return s-1
#
# print(task(80))



# def task(n, m, k):
#     a = n + m
#     b = n + k
#     c = k + m
#     f = ((n, m) if a > b and a > c else ((n, k) if b > c and b > a else (k, m)))
#     return f
#
# print(task(2, 22, 9))

# a = list('salom')
# print(a)



# fruits = ['olma', 'anor', 'gilos', 'uzum', 'nok', 'banan']
# print(type(fruits))
# print(fruits)
# print(fruits[start:stop:step])
# print(fruits[::2])
# print(len(fruits))
# a = list()
# f = list((23, 89))
# b = []
# print(a, b, f)
# fruits = ['olma', 'anor', 'gilos', 'uzum', 'nok', 'banan']
# fruits[2:4] = []
# print(fruits)
# fruits.append(('tarvuz'))
# fruits.append(('qovun'))
# fruits.insert(3, 'kiwi')
# del fruits
# fruits.clear()
# fruits.sort()
# a = sorted(fruits)
# fruits.reverse()
# fruits = ['olma', 'anor', 'gilos', 'uzum', 'nok', 'banan', 'uzum']
# a = fruits.copy()
# fruits.append('qovun')
# print(a)
# print(fruits.count('uzum'))
# print(fruits.index('uzum'))



# fruits = ['olma', 'anor', 'gilos', 'uzum', 'nok', 'banan', 'uzum']


# a = [1, 6, 1, 2, 4, 1, 9]
# def summ(a):
#     s = 0
#     for i in a:
#         s += i
#     return s
# print(summ(a))

# a = [1, 6, 1, 2, 4, 1, 9, 10]
# print(a)
#[1, 1, 1, 9]
# def main(list):
#     x, y = [], []
#     for i in list:
#         if i % 2 == 0:
#             x.append(i)
#         else:
#             y.append(i)
#     return x, y
#
# print(main(a))

# fruits = ['olma', 'anor', 'gilos', 'uzum', 'nok', 'banan', 'uzum']
# for i in fruits:
#     if fruits.count(i) > 1:
#        for j in range(fruits.count(i)):
#             fruits.remove(i)
#
# print(fruits)