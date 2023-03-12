#__call__

class Dog:
    def __init__(self,name):
        self.name = name

    def __call__(self,age):#类似于偏函数
        print('名字是%s,年龄是%d' % (self.name,age))


d = Dog('Tom')
print(d.name)
d(18)
d(20)
#d.age 会报错没有该属性