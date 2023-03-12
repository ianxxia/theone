
def test1():#无参数
    print(3 ** 2)

test1()

def test1(x): #参数 形参
    print(x ** 2)

test1(2)#实参

def zhiding(m,n):
    print('+++++++'*50)
    print(m * 3)
    print(n ** 3)

zhiding(n=3,m=2)#指定形参赋值

def defultfun(m=3):
    print(m ** 2)


defultfun()#不输入实参默认为3

