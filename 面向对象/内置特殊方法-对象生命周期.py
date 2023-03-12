class Cat:
    def __new__(cls, *args, **kwargs): #输出111
        print('111')

    def __init__(self):#不输出 需要输入参数
        print('222')

    def __del__(self):#释放对象
        print('333')

c = Cat()
del c
print(c)