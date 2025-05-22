from time import time
# def kvadrat(x):
#     return x**2

# # print(kvadrat(3))
#
# a = lambda x: 0 if x == 0  else 'juft' if x % 2 == 0 else 'toq'
#
# print([a(i) for i in range(10)])

# dct = {
#     'a': 111, 'n': 21, 'c': 32
# }
# print(sorted(dct.items(), key=lambda x: x[0]))



#map

data = [i for i in range(1_000_000)]
# def test_map(data):
#     result = []
#     for i in data:
#         result.append(i**2)
#     return result
#
# print(test_map(data))


# start = time()
# result = []
# for i in data:
#     result.append(kvadrat(i))
# print(result)
# finish = time()
# print(finish-start)


# start = time()
# result = list(map(lambda x: x**2, data))
# print(result)
# finish = time()
# print(finish-start)


# result = list(filter(lambda x: x % 2 == 0, data))
# print(result)


# words = ['apple', 'banana', 'kiwi', 'grape']
# a = list(map(lambda x: len(x), words))
# print(a)

# a = [2, 4, 6]
# b = [3, 5, 7]
# c = [2, 4, 0]
# # print(list(map(lambda x, y, z: x*y*z, a, b, c)))

# nums = [10, 15, 20, 25, 30]
# # k = list(map(lambda x: x*5, nums))
# # print(k)
# print(list(filter(lambda x: x < 100, (map(lambda x: x*5, nums)))))


text = ['hello', 'python', 'django', 'o\'rik', 'Olma', 'ilon', 'O\'lmas']
unli = ['a', 'e', 'i', 'o', 'u', 'o\'']
print(list(filter(lambda x: x[0].lower() in unli, text)))

# def tub_emas():
#     pass
#
#
# filter(lambda x: tub_emas(x), data)




