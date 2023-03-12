# # class Cad:
# #     name = "qq"
# #
# #     def __init__(self):
# #         self.name = 'tom'
# #         self._age = 19
# #         self.__money = 100
# #
# #
# #     def getMoney(self):#只读 先私有化一个属性 然后通过函数返回值 就是只读
# #         return self.__money
# #
# #
# # c = Cad()
# # print(c.getMoney())
#
# class Cad:
#     name = "qq"
#
#     def __init__(self):
#         self.name = 'tom'
#         self._age = 19
#         self.__money = 100
#
#     def setmoney(self,val):
#         #输入的资金必须为整数且大于0
#         if(isinstance(val,int) and val >= 0 ):
#             self.__money -=val
#         else:
#             print('请输入正确的金额')
#
#     # @property#通过装饰器 将函数当做属性使用
#     def getMoney(self):#只读 先私有化一个属性 然后通过函数返回值 就是只读
#         return self.__money
#
#     def delMoney(self):
#         del self.__money
#     money = property(getMoney,setmoney,delMoney)
#
# c = Cad()
# print(c.getMoney)#<bound method Cad.getMoney of <__main__.Cad object at 0x0000021D
# print(c.money)#100
# c.money = 89
# print(c.money)#11

class Person:
    def __init__(self):
        self.name = 'Tom'
        self.__money = 100

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self,val):
        self.__money = val

p = Person()
print(p.money)#100
p.money = 33
print(p.money)#33

