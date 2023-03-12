

class Person:
    def __init__(self):
        self.name = 'Tom'

    def __setattr__(self, key, value):#对属性进行预处理
        print(key,value)
        if key == 'age' and key in self.__dict__.keys():
            print('只读属性不许修改')
        else:
            self.__dict__[key] = value#{'name': 'Tom', 'age': 19}

p =Person()
print(p.__dict__)#{}
p.age = 19
print(p.__dict__)#{}
p.age = 12
print(p.__dict__)#只读属性不许修改
                   # {'name': 'Tom', 'age': 19}