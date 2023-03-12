

import abc
class Person(object,metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def eat(self):
        print('www')


    def jump(self):
        print('xxx')


#p = Person()#TypeError: Can't instantiate abstract class Person with abstract methods eat
class Man(Person):#必须要重写抽象方法 箭头往上代表重写上面方法
    def eat(self):
        print('已重写抽象方法')
    pass

    def f(self):
        print('ooooo')

m = Man()
m.eat()#TypeError: Can't instantiate abstract class Man with abstract methods eat
m.f()


