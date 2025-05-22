# 2
# def main(n):
#     return [2**i for i in range(n+1)]
#
# print(main(5))


# 6
# def main(n):
#     a = 0
#     b = 1
#     for i in range(n):
#         a, b = b, a+b
#         print(b)
# main(5)


#6
# def main(n, a, b):
#     d = [a, b]
#     for i in range(2, n):
#         d.append(sum(d))
#     return d
# print(main(5, 10, 1))

#33
# def main(s1, s2):
#     a = s1.replace(s2, '', 1)
#     return a
#
# print(main('World Hello World', 'World'))


# D = {
#     'emp1': {'name': 'Bob', 'job': 'Mgr'},
#     'emp2': {'name': 'Kim',  'job': 'Dev'},
#     'emp3': {'name': 'Sam', 'job': 'Dev'}
#      }
# l = []
# for i in D.values():
#     l.append(i['name'])
# print(l)

# my_list = [2, 7, 9, 10, 11, 12, 13, 14, 15]
# def main(n):
#     d = {}
#     for i in my_list:
#         d.update({i: 'JUFT'}) if i % 2 == 0 else d.update({i: 'TOQ'})
#     return d
# print(main(5))
#
#
# my_list = [2, 7, 9, 10, 11, 12, 13, 14, 15]
# # my_dict ={2:'juft'', 7:'toq', ...}




# a = {2: 'JUFT', 7: 'TOQ', 9: 'TOQ', 10: 'JUFT', 11: 'TOQ', 12: 'JUFT', 13: 'TOQ', 14: 'JUFT', 15: 'TOQ'}
# b = {2:'qwefq', 4: 'JUFT', 5: 'JUFT', 6: 'wef'}
# c = b | a
# print(c)

# D = {
#     'emp1': {'name': 'Bob', 'job': 'Mgr'},
#     'emp2': {'name': 'Kim',  'job': 'Dev'},
#     'emp3': {'name': 'Sam', 'job': 'Dev'}
#      }
#
# for i in D.values():
#     if i['job'] == 'Dev':
#         i['maosh'] = 1500
#     else:
#         i['maosh'] = 500
# print(D)





# D = {
#     'emp1': {'name': 'Bob', 'job': 'Mgr', 'maosh': 500},
#     'emp2': {'name': 'Kim',  'job': 'Dev', 'maosh': 1500},
#     'emp3': {'name': 'Sam', 'job': 'Dev', 'maosh': 1500}
#      }

