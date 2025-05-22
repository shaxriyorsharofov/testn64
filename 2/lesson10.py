# # a = [10, 1, 2, 3, 2, 2, 2, 1, 56, 78]
# def test(lst):
#     result = []
#     d = [lst[0]]
#
#     for i in range(1, len(lst)):
#         if lst[i] >= lst[i-1]:
#             d.append(lst[i])
#         else:
#             if len(d) > 1 and len(d) != d.count(d[0]):
#                 result.append(d)
#             d = [lst[i]]
#     if len(d) > 1 and len(d) != d.count(d[0]):
#         result.append(d)
#     return result

#
# # a = [10, 1, 2, 113, 200, 2, 2000, 1000, 56, 78]
# def test_(lst):
#     sum_lst = []
#     for i in range(1, len(lst)):
#         sum_lst.append(lst[i] + lst[i - 1])
#     return lst[sum_lst.index(max(sum_lst))], lst[sum_lst.index(max(sum_lst))+1]
#

# from oy_1.test import temp
# from oy_1.lesson2 import kopaytirish
# from oy_1 import temp_, kopaytirish

# print(temp_(2, 7))
# print(kopaytirish(2, 7))



# if __name__ == '__main__':
#     print(test_([10, 1, 2, 3, 2, 2, 2, 1, 56, 78]))
#     print('afqwefgqewrgf')




# a = [12, 13, 14, 15, 16, 17, 18, 19, 20, 25]
# b = a[3::3]
# print(len(b), b)








