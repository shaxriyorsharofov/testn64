# 4

# a = [1, 1, 3, 4, 4, 5, 6, 7]
# b = [0, 1, 2, 3, 4, 4, 5, 7, 8]
# def orta_arifmetik(a, b):
#     a.extend(b)
#     return sum(a)/len(a)
#
# print(orta_arifmetik(a, b))


# 8

# a = [112, 11, 2, 13, 41, 58, 69, 7]
# # print(a[::2][::-1])
# def main(a):
#     l = a[::2][::-1]
#     n = 0
#     for i in range(0, len(a), 2):
#         a[i] = l[n]
#         n += 1
#     return a
# print(main(a))


# def change_even(lst:list)->list:
#     even_nums = lst[0::2][::-1]
#     counter = 0
#     for i in range(len(lst)):
#         if i%2==0:
#             lst[i] = even_nums[counter]
#             counter+=1
#     return lst
# b = [0, 1, 2, 3, 4, 5, 6, 7]
# print(change_even(b))

# 9

# a = [112, 11, 2, 13, 41, 58, 69, 7]
# def tub(a):
#     b = []
#     for i in a:
#         n = 0
#         for j in range(1, i+1):
#             if i % j == 0:
#                 n += 1
#         if n == 2:
#             b.append(i)
#
#     return b
#
# print(tub(a))


# 11

# a = [112, 11, 2, 13, 41, 58, 69, 7]
# b = [112, 10, 4, 11, 2, 45]
#
# def cub(a, b):
#     c = []
#     for i in a:
#         for j in b:
#             if i == j:
#                 c.append(i)
#     return c
#
# print(cub(a,b))


# a = (112, 11, 2, 13, 41, 58, 69, 7)
#
#
# # result = (f"{i}: juft" if i % 2 == 0 else f"{i}: toq" for i in a if i < 100)
#
# B = tuple(i for i in a if i % 2 == 0)
#
#
# print(B)
#
#
# A = 'aqfdwqef'
# B = 'MK'
# print(str(A) + B)


# a = [1, 4, 3, 9]
# b = "RM"
# def test(a, b):
#     # return [b+str(i) for i in a]
#     l = []
#     for i in a:
#         l.append(b + str(i))
#     return l
# print(test(a, b))



# a = """Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the
# industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and
#  scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap
#  into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the
#   release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing
#   software like Aldus PageMaker including versions of Lorem Ipsum"""

# a = 'a-b-c-d-e-f'
# print(a.rsplit('-', 2))

# b = ['ab', 'sw', 'hf', 'eb', 'wer']
#
# result = '*'.join(b)
# print(result)
#
# print("My name is {} {}".format("Ali", 'wefqe'))
# print("My email is %s" % '25')


# def main(n, a):
#     if len(a) > n:
#         return a[-n:]
#     else:
#         nuqta = (n - len(a)) * '.'
#         return nuqta + a
#
# print(main(3, 'salom'))


telefon
fon

tg
teletgfon

