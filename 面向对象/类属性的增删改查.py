

class Person(object): #在python2内 这样写法叫经典类 pytho3
    #默认继承object
    #属性
    name = 'xxx'
    age = 19
    # 方法
    def eat(self):
        print('吃饭')

    def run(self):
        print('跑步')

p = Person()
print(Person.__dict__)
Person.top = 180 #增加
Person.age = 22#修改
p.a = 88#通过对象无法给类增删改查
p.name = 'QQ'#{'a': 88, 'name': 'QQ'}
print(p.__dict__)
print(Person.__dict__)#增加top属性

del Person.top#删除

#查找 先查找对象是否有这个属性 没有再从类找
s = Person()
s.name = 'cx'
print(Person.name)#xxx
print(s.name)#cx
