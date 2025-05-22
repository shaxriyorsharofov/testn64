# from uuid import uuid4
# import random
# # print(str(uuid4()).split('-')[0])
#
#
# # class Users:
# #     def __init__(self, id=uuid4()):
# #         self.id = id
#
#
# # id = "".join([str(random.randint(0, 1_000_000))[-1] for _ in range(4)])
#
# # print(id)
#
#
#
#
#
# class Users:
#     def __init__(self, name, age, prof, id=uuid4()):
#         self._id = id
#         self.name = name
#         self.age = age
#         self.__prof = prof
#
#     def get_info_user(self):
#         return self.name
#
#     def get_prof(self):
#         return self.__prof, self._id


# u1 = Users('Xayrullox', 15, 'Python')
# print(u1.name)
# print(u1._id)
# print(u1.get_prof())


# class Ishchi(Users):
#     def __init__(self, name, age, prof, kunlik, dollor, kun, id=uuid4()):
#         Users.__init__(self, name, age, prof, id=uuid4())
#         self.__kunlik = kunlik
#         self.__dollor = dollor
#         self.kun = kun
#
#     def get_maosh(self):
#         return self.__kunlik * self.__dollor * self.kun
#
#     def get_id(self):
#         return self._id
#
#     def set_prof(self, p):
#         self.__prof = p


# i1 = Ishchi('Javohir', 19, 'Java', 200, 12900, 20)
# print(i1.get_maosh())
# print(i1.get_prof())
# i1.set_prof('Go')



from abc import ABC, abstractmethod

class Hayvonlar(ABC):

    @abstractmethod
    def ovoz(self):
        pass

    @abstractmethod
    def see(self):
        pass

    @abstractmethod
    def ovqat(self):
        pass


class Dog(Hayvonlar):
    def __init__(self, name):
        self.name = name

    def ovoz(self):
        return 'vov vov'

    def see(self):
        return True

    def ovqat(self):
        return "gosht"


d1 = Dog('Simba')
print(d1.name)


class Mushuk(Hayvonlar):
    pass









