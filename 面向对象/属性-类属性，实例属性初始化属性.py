class Person:

    sex = '男' #类属性

    def __init__(self,name):#对象初始化属性
        self.name = name
        self.a = 100



p = Person('jerry')
p.age = 19 #对象属性
print(p.sex)
print(p.name)