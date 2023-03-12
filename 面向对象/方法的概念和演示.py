class Person(object):
    def run(self):
        print("pao",self)#<__main__.Person object at 0x000001D2DA4AA240>

    def eat(self):
        print("chi")

p = Person()
p.run()
str = 'asd'
print(str.find('d'))
print(p)#<__main__.Person object at 0x000001D2DA4AA240>
#p=self

p2 = Person()
p2.run()
print(p2)
#谁调用方法 self就是谁