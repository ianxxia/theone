

#键值对查找

#__setitem__ __getitem__ __delitem__


class Cat:
    def __init__(self):
        self.its = [1,2,3,4,5,6]

    def __setitem__(self, key, value):
        print(key,value)#slice(1, 4, 2) ['a', 'b']
        print(key.start)#1
        print(key.stop)#4
        print(key.step)#2
#原理        if isinstance(key,slice):
#原理            self.its[key.start:key.stop:key.step] = value

    def __getitem__(self, item):
        return self.its[item]


    def __delitem__(self, key):
        del self.its[key]
        print('删除键值对',key)
# slice
c = Cat()
print(c[1:4:2])
# c[1:4:2] = ['a','b']

