class Person(object): #在python2内 这样写法叫经典类 pytho3
    #默认继承object
    #属性
    name = 'xxx'
    age = 19

p = Person() #类属性不可变 对象属性可变
p.name='QQ'
print(p.__dict__)
p.__dict__ = {'name':'chenxian'}
print(p.__dict__)

Person.age = 55
print(Person.__dict__)#{'__module__': '__main__', 'name': 'xxx', 'age': 55, '__dict__':

# Person.__dict__['age'] = 35#不能修改 TypeError: 'mappingproxy' object does not support item assignment
# print(Person.__dict__)
Person.__dict__ = {'__module__': '__main__', 'name': 'xxx', 'age': 55,}
print(Person.__dict__)#不能写入 AttributeError: attribute '__dict__' of 'type' objects is not writable