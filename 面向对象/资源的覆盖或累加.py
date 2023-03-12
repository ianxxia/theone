#
# class Person:
#     name = 'jerry'
#
#     def run(self):
#         print('pao')
#
#
# class  man(Person):
#
#     name = 'Tom' #属性重写 覆盖
#
#     def run(self): #方法重写 累加
#         print('跑重写函数')
#
#
#     pass
#
#
# m = man()
# print(m.name)
# m.run()


class person():
    def __init__(self):
        self.age = 18

    @classmethod
    def eat(cls):
        print('吃饭啦')

    @staticmethod
    def sleep():
        print('睡觉啦')

#通过调用父类的init方法 解决方法1
# class man(person):
#     def __init__(self):
#         person.__init__(self)
#         self.sex = 'man'

class man(person):
    def __init__(self):
        super().__init__()
        self.sex = 'man'

m = man()
print(m.age)
# print(man.age)


#使用super来调用父类的属性 解决方法2