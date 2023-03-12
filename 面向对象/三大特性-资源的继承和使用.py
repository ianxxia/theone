

#继承关系中资源的调度 资源的继承和实用
#资源的覆盖和累加

class Person:

    name = 'tom' #公有
    _age = 18 #受保护属#
    __sex = '男' #私有属性


    def __init__(self):
        print('init方法')

    def func1(self):
        print('公有方法')

    def _func2(self):
        print('受保护方法')

    def __func3(self):
        print('私有方法')

#上述统称为资源

class Dad(Person):
    @classmethod
    def func(cls):
        print(cls.name)
        print(cls._age)
        cls._age = 20#增加了一个属性 非修改父类的属性
        print(cls._age)
        #print(cls.__sex)

    def test(self):
        self.func1()
        self._func2()
        #self.__func3()


# Dad.func()
#
# d = Dad()
# d.test()

class  Sun(Dad):
    pass


print(Sun.mro())#mro查找继承关系
#[<class '__main__.Sun'>, <class '__main__.Dad'>, <class '__main__.Person'>, <class 'object'>]
