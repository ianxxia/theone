#私有化属性和受保护属性
class Person:
    name = 'jerry' #公有属性 普通类属性
    _age =19 #受保护属性
    __sex = '男' #私有化属性

    def eat(self):
        print(self.name)#三个都可以访问 通过self
        print(self._age)
        print(self.__sex)
        pass

p =Person()
p.eat()

#jerry
#19
#男
# print(p.age)
# print(Person.name)
print(p.name)
print(p._age)#能调用但最好不要调用
print(p.__sex)#无法调用


#总结公有属性 通过类的内部 对象调用 子类调用 模块之间的调用都能访问
#受保护的属性 通过类的内部可以访问 对象调用 子类调用模块调用也能强行访问但有黄色波浪线提示
#私有属性 一般只能在类的内部访问