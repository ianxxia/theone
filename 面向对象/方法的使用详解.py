class Person:
    name = 'Tom'
    list = ['tome','cat','kk']
    def eat(self):
        print('他在吃饭',self)
        print(self.name)
        print(self.age)

    @classmethod
    def run(cls):
        print('他在跑步',cls)
        print(cls.name)
        #print(cls.age)#AttributeError: type object 'Person' has no attribute 'age'
        #类方法无法访问类外部的属性 age

    @staticmethod
    def hah():
        print('他在笑')
        print(Person.name)#可以访问Tom
        # print(Person.age)#AttributeError: type object 'Person' has no attribute 'age'

p = Person()
p.age = 18
p.eat()
p.hah()
print(p.list.index('tome'))

#实例方法 可以访问类属性和实例属性
#
#类方法 不能访问实例属性
#静态方法 不能访问实例属性

