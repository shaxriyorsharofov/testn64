#7

# d1 = {'a': 100, 'b': 200, 'c': 300}
# d2 = {'a': 300, 'b': 200, 'd': 400}
#
#
# result = d1.copy()
# for key, value in d2.items():
#     if key in result:
#         result[key] += value
#     else:
#         result[key] = value
# print(result)


# a = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
# def test_(dict_):
#     result = []
#     for i in dict_:
#         for k in i.values():
#             result.append(k)
#     return [i for i in result if result.count(i) == 1]
#
# print(test_(a))

#9
# a = 'assalom'
# print({i: a.count(i) for i in a})


# a = 'mexanizasiyalashtirilganmiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii'
# def test(a):
#     myd = {i: a.count(i) for i in a}
#     print(myd)
#     x = max(myd.values())
#     return [f"{i}:{j}" for i, j in myd.items() if j == x]
#
# print(test(a))

#
#
# a='mexanizasiyalashtirilganmi'
# x=list(a)
# dict1={}
# mylist=[]
# for i in range(len(a)):
#     dict1.update({x[i]:x.count(x[i])})
# for j in dict1.values():
#     mylist.append(j)
# maxwe=max(mylist)
# for l,n in dict1.items():
#     if n==maxwe:
#         print(f"{l}:{maxwe} marta eng kob takrolangan")
#
#
#
#
# # a = "mexanizasiyalashtirilganmi"
# # h = {}
# # for i in a:
# #     if i in h:
# #         h[i]+=1
# #     else:
# #         h[i]=1
# #     c = max(h.values())
# # for key, value in h.items():
# #     if value == c:
# #         print(f"{c} ta {key} harfi bor")
#
#
#
# def main(s):
#     lst = list(s)
#     dic = {i:lst.count(i) for i in lst}
#     first = list(dic.keys())[0]
#     for i in dic:
#         if dic[i] > dic[first]:
#             first = i
#     return f"element:{first}, element count: {dic[first]}"
# print(main("mexanizatsiyalashtirilganmi"))




# a = {1:'qwefqer', 2:'cc', 3:'qwefccccqew'}
# print(max(a.keys()))


d = {
    1: '12',
    2: 321,
    3: 'a',
    4: 2132,
    5: 'b4',
    6: 'gjjg'
}

# d = {
#     1:'e',
#     2:'b',
#     3:'c',
#     4:'d',
#     5:'a'
# }

# a = 'ASSALOM Uzb'
# # u = [unlilar ]
# q = {'unli':[], 'undosh':[]}


# a=input("matn kiriting:")
# kiril_lotin = {
#         "ё": "yo", "ю": "yu", "я": "ya",
#         "а": "a", "б": "b", "д": "d", "е": "e", "ф": "f", "г": "g", "ҳ": "h",
#         "и": "i", "ж": "j", "к": "k", "л": "l", "м": "m", "н": "n", "о": "o",
#         "п": "p", "қ": "q", "р": "r", "с": "s", "т": "t", "у": "u", "в": "v",
#         "х": "x", "й": "y", "з": "z"
#         }
# for kiril, lotin in kiril_lotin.items():
#     a = a.lower().replace(kiril, lotin)
# # print(a)





# krill_lotin = {
#     "А": "A", "Б": "B", "В": "V", "Г": "G", "Д": "D", "Е": "E", "Ё": "Yo", "Ж": "J", "З": "Z",
#     "И": "I", "Й": "Y", "К": "K", "Қ": "Q", "Л": "L", "М": "M", "Н": "N", "О": "O", "П": "P",
#     "Р": "R", "С": "S", "Т": "T", "У": "U", "Ф": "F", "Х": "X", "Ҳ": "H", "Ч": "Ch", "Ш": "Sh",
#     "Ъ": "'", "Э": "E", "Ю": "Yu", "Я": "Ya",
#     "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e", "ё": "yo", "ж": "j", "з": "z",
#     "и": "i", "й": "y", "к": "k", "қ": "q", "л": "l", "м": "m", "н": "n", "о": "o", "п": "p",
#     "р": "r", "с": "s", "т": "t", "у": "u", "ф": "f", "х": "x", "ҳ": "h", "ч": "ch", "ш": "sh",
#     "ъ": "'", "э": "e", "ю": "yu", "я": "ya"
# }
# soz = input("sozni kiriting:")
# k = []
# for i in range(len(soz)):
#     k.append(krill_lotin.get(soz[i]))
# gamma = k[0]
# for i in range(1, len(k)):
#     gamma = gamma+k[i]
# print(gamma)

# set1 = {10, 20, 30}
# set2 = {20,40,50}
#
# set1.difference_update(set2)
# print(set1)



# print(d := {i: i**2 for i in {10, 20, 30}})


# print({i for i in range(10)})