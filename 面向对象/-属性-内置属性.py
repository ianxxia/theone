'''
1 类属性
__dict__ 所有类属性和类方法 -字典
__bases__ 所有的父类-元祖
__doc__ 类的文档-字符串
__name__ 类的名字
__module__ 类所在的模块

2.实例属性
__dict__ 实例的所有属性和方法
__class__ 实例对应的类

'''


class A:
    pass

class Person(A):
    """"123345566778"""
    sex = '男'
    def __init__(self):
        self.name  = 'ton'
        self.__money = 100



#property
p = Person()
print(Person.__dict__)
print(p.__dict__)
print(Person.__base__)#<class 'object'> <class '__main__.A'>
print(Person.__doc__)#"123345566778
print(Person.__module__)#__main__
