
#6
# a = [1, 6, 9, 90]
# b = [1, 2, 3, 4, 5, 6, 7, 8]
# def test_(a, b):
#     d = []
#     for i in a:
#         if i in b:
#             d.append(True)
#     return d
# print(test_(a, b))

# a = [1, 2, 3, 4, [2, 9, [3, 9, 7], 9], 5, 6, 7, 8]
# print(a[4][2][1])

# a = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum"
# b = a.split()
# print(b)


# a = "salom python assalom python salom dunyo"
# def main(a):
#     b = a.split()
#     b_copy = b.copy()
#     for i in b:
#         if b_copy.count(i) > 1:
#             b_copy.remove(i)
#     for j in b_copy:
#         print(f"{j}: {b.count(j)}")
#
# main(a)


# a = ('olma', 'anor', 'gilos')
# def main(b):
#     my_list = list(a)
#     my_list.append(b)
#     return tuple(my_list)
#
# print(main('banan'))

# a = ('olma', 'anor', 'gilos')
# def main():
#     my_list = list(a)
#     return tuple(my_list[::-1])
#
# print(main())



# a = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# def main(n):
#     result = []
#     for i in a:
#         x = list(i)
#         x[-1] = 100
#         result.append(tuple(x))
#     return result
#
# print(main(100))

a = [191, 20, 211, 2, 2354]
# print(min(a))
min_a = a[0]
for i in a:
    if i < min_a:
        min_a = i
print(min_a)


