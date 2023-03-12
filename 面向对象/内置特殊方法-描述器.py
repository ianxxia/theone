#
# class Dog(object):
#     def __init__(self):
#         self.__age = 18
#
#     def get_age(self):
#         return self.__age
#
#
#     def set_age(self,val):
#         if val < 0:
#             val = 0
#         self.__age = val
#
#     def del_age(self):
#         del self.__age
#
#     age = property(get_age,set_age,del_age)
#
# d = Dog()
#
# d.set_age(5)
#
# print(d.get_age())
# help(Dog)

class Age:
    def __get__(self,instance,owner):
        print('get',instance,owner)

    def __set__(self,instance,value):
        # print('set',instance,value)
        if value > 3:
            print('成年了')

    def __delete__(self, instance):
        print('del',instance)


class Dog:
    age = Age()

d= Dog()
d.age = 5
print(d.age)