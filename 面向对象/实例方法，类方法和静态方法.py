class Dog:
    def run(self):
        print('实例方法',self) #实例对象

    @classmethod
    def shout(cls): #类
        print('类方法',cls)

    @staticmethod
    def eat():
        print('静态方法')


d = Dog()#实例方法 <__main__.Dog object at 0x000001FC19DEB0B8>
d.run()

Dog.run(d) #必须传入对象d 实例方法 <__main__.Dog object at 0x000001D50999B0B8>

Dog.shout()#类方法 <class '__main__.Dog'>
d.shout()#类方法 <class '__main__.Dog'>

d.eat()#直接使用 静态方法

print(Dog.__dict__)#{'__module__': '__main__', 'run': <function Dog.run at 0x0000024361513F28>, 'shout': <classmethod object at 0x000002436139B0B8>, 'eat': <staticmethod object at 0x000002436139B080>, '__dict__': <attribute '__dict__' of 'Dog' objects>, '__weakref__': <attribute '__weakref__' of 'Dog' objects>, '__doc__': None}