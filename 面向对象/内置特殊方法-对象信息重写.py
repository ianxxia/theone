class Dog:
    name = 'Tom'

    def __init__(self):
        self.sex = 'man'
        self.age = 19

    def __str__(self):#偏向用户
        #可以返回类的自定义说明信息
        return '%s,%s,%d '%(Dog.name,self.sex,self.age)

    def __repr__(self):#偏向开发人员
        a = '傻逼类'
        return a
d = Dog()
print(d)#Tom,man,19

print(repr(d))#<__main__.Dog object at 0x000002A0CE03A0F0>
