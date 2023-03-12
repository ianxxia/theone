class Person:
    def __init__(self,age):
        self.age = age

    def __bool__(self):
        return self.age >= 18


p = Person(25)#p是bool
print(p)
if p :
    print('p是bool')
else:
    print('p not bool')

