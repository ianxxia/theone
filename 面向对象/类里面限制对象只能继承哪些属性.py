class Person(object):
    __slots__ = ['sex','aa']
    name = 'xxx'
    age = 19

p1 = Person()
#p1.bb = 33#没有该属性AttributeError: 'Person' object has no attribute 'bb'
p1.aa = 33 #没问题