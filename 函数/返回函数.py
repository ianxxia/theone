#当一个函数的返回结果是另一个函数的时候
#这样的函数即为返回函数

age = input("输入年龄")


def fun1(a):

    def fung(x):
        print("够岁数了")
        return 'hah够了{}'.format(x)

    def funl(x):
        print("五够岁")
        return 'ha5够aaa{}'.format(x)

    if(int(a)>=18):
        return fung
    else:
        return funl

res = fun1(age)
print(res(19))#ha5够aaa19
print(type(res))#<class 'function'>