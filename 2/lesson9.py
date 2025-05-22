# # 63
# alfavit = [
#      "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
#     "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
#     "V", "X", "Y", "Z"
# ]
# def main(soz, k):
#     result = ''
#     for a in soz:
#         if alfavit.index(a) + k > len(alfavit) - 1:
#             result += alfavit[alfavit.index(a) + k - len(alfavit)]
#         else:
#             result += alfavit[alfavit.index(a) + k]
#     return result
# print(main('VXY', 3)) #ZAB



# #65
# alfavit = [
#      "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
#     "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
#     "V", "X", "Y", "Z"
# ]
# def main(kodlangan, asil_qiymat):
#     return alfavit.index(kodlangan[0]) - alfavit.index(asil_qiymat)
# print(main('ZAB', 'V'))


#69

# def main(matn):
#     if matn.count('(') == matn.count(')') and matn.rfind(')'):
#         return 0
#     elif matn.count('(') > matn.count(')'):
#         return matn.rfind('(')
#     else:
#         return -1
# print(main('((as))'))



#66
# def main1(satr):
#     return satr[::2] + satr[1::2][::-1]


# 67

# def main(satr):
#     result = ''
#     if len(satr) % 2 == 0:
#         toq = satr[len(satr)//2:][::-1]
#         juft = satr[:len(satr)//2]
#         for i in range(len(satr)//2):
#             result += juft[i]
#             result += toq[i]
#     else:
#         toq = satr[len(satr) // 2+1:][::-1]
#         juft = satr[:len(satr) // 2+1]
#         for i in range(len(satr) // 2):
#             result += juft[i]
#             result += toq[i]
#     return result + juft[-1]
# print(main1('Shaxriyor')) #Saryroixh
# # print(main('Saryroixh'))


# data = [2, 5, 8, 11, 1]

# def main(data):
#     d = data[1] - data[0]
#     for i in range(1, len(data)):
#         if data[i] - data[i-1] != d:
#             result = False
#         else:
#             result = True
#     return result
# print(main(data))


# def juft_toq(data):
#     return [j for j in [i if data.index(i) % 2 == 0 and i < 0 else \
#                 i if data.index(i) % 2 == 1 and i > 0 else '' for i in data] if len(str(j))>=1][0]
#
# print(juft_toq([12, -13, -14, -15, -10, 11]))



# def test(data):
#     results = []
#     for i in range(1, len(data)):
#         if data[i] < data[i - 1]        :
#             results.append(data.index(data[i-1]))
#     return sorted(results)
#
# print(test([11, 2, 13, 4, 15]))



