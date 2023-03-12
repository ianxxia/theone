#键值对查找

#__setitem__ __getitem__ __delitem__


class Cat:
    def __setitem__(self, key, value):
        print('设置键值对',key,value)

    def __getitem__(self, item):
        print('获得键值对',item)

    def __delitem__(self, key):
        print('删除键值对',key)

c = Cat()
c['age'] = 19
print(c['age'])
print(c.__dict__)
print(Cat.__dict__)
