from itertools import combinations
#
# sozlar = ["listen", "silent", "hello", "world", "enlist", "python", "typhon"]


# lst = []
# for i in range(len(sozlar)):
#     for j in range(i+1, len(sozlar)):
#         for g in range(j+1, len(sozlar)):
#             lst.append((sozlar[i], sozlar[j], sozlar[g]))
# print(len(lst))


# sozlar_ = list(combinations(sozlar, 3))
# print(len(sozlar_))
# func_ = lambda x: sorted(x[0]) == sorted(x[1])
# print(list(filter(func_, sozlar_)))




# data = ["hello", "world", "python", "programming"]
# result = list(map(lambda word: ''.join([i for i in word if i.lower() not in "aeiou"]), data))
#
# print(result)


# data1 = ["hello", "world", "python", "pg"]
# data2 = ["listen", "si", "hello", "world"]
# # data = list(zip(data1, data2))
# # print(data)
# print(list(filter(lambda x: len(x[0] + x[1]) > 10, list(zip(data1, data2)))))


# lst = ['SaLom', "PYt1ON", "DjaNgO"]

#2
# for i in lst:
#     ki = 0
#     ka = 0
#     for j in i:
#         if j.isupper():
#             ka += 1
#         else:
#             ki += 1

# a = list(map(lambda x: (sum([1 for i in x if i.isupper()]), sum([1 for i in x if i.islower()])), lst))
# print(a)


#3
# a = 7
# data = [4, 9, 0, 34, 78, 3, 7]
# juftlar = list(filter(lambda x: x % 2 == 0, data))
# farqlar = list(map(lambda f: (abs(f - a), f), juftlar))
# sort_ = sorted(farqlar)
# print(sort_[0][1]**2)


#5
# b = [20, 30, 60, 10]
# c = [30, 40, 10, 80]
a = [11, 23, 35, 40]
#
# print(list(filter(lambda x: sum(x) > 100, zip(a, b, c))))


#6
import math


# print(list(map(lambda x: sum([math.factorial(int(i)) for i in str(x)]), a)))

# print((min(sorted(list(map(lambda f: (abs(f - a), f), filter(lambda x: x % 2 == 0, data)))))[1])**2)

# nums = [11, 22, 35, 40]
# count = 34
# a = min(filter(lambda x: x % 2 == 0, nums), key=lambda x: abs(x - count))
# result = a ** 2
# print(result)




# lst = ['salom', "python", "django"]
# print("".join(sorted(lst[1], reverse=True)).capitalize())
# print(list(map(lambda x: sorted(x))))



# nums = [11, 22, 35, 40]

# print(list(map(lambda x: sum(int(i) for i in str(x)), nums)))

# nums = [11, 22, 35, 40]
# print(list(enumerate(nums)))
# print(list(map(lambda x: x[0] * x[1], enumerate(nums))))









# soz = ['salom', 'dastur', 'kaktus', 'roman', 'taom']
# print(list(filter(lambda x: x[-1] in 'amn', soz)))


# soz = ['hi', 'salom', 'programming', 'kitob']
# print(list(map(lambda x: 'short' if len(x) < 5 else 'medium' if 8 >= len(x) >= 5 else 'long', soz)))















