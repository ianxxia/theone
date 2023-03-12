class person:
    age = 18
    name = 'xxx'
    top = 'ddd'

    pass

#由类到对象叫做 实例化
#由对象到类叫做 抽象化

class Note: #在python2内 这样写法叫经典类 pytho3
    #默认继承object
    #属性
    name = 'xxx'
    age = 19
    # 方法
    def eat(self):
        print('吃饭')

    def run(self):
        print('跑步')

print(Note.__base__)#<class 'object'> 基类

p = person()
n = Note()
print(p.name)#xxx
print(n.eat())#吃饭 None
#输出None是因为没有return 
p.sex = '男' #对象属性 类属性里没有
print(p.__dict__)
print(person.__dict__)
print(p.sex)
p.sex = '女'
print(p.sex)#女 修改对象属性
p.top = 180#原来没有top属性 这操作叫新增非赋值

del p.sex
print(p.sex)#已删除该属性AttributeError: 'person' object has no attribute 'sex'
