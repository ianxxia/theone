
#元类 就是用来创建类这个对象到基础类
#通俗来说就是最底层的类

num = 10
str1 = 'aaaa'
class A:
    pass

aa = A()

# print(num.__class__)#<class 'int'>
# print(num.__class__.__class__)#<class 'type'>
#
# print(str1.__class__)#<class 'str'>
# print(str1.__class__.__class__)#<class 'type'>
#
# print(aa.__class__)#<class '__main__.A'>
# print(aa.__class__.__class__)#<class 'type'>

def run(self):
    print('wwwwwww')
aa = type('Cat',(),{'name':'Tom','run':run})
#第一个参数类名 第二个参数父类（多继承） #
# 第三个方法属性 通过字典实现
d = aa()
d.run()#wwwwwww

print(d.name)#Tom