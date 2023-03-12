#在嵌套函数中 内部函数引用外部函数的参数
#和变量所获得的结果，被外层函数当做返回值
#给返回的情况叫做闭包函数

def func(m):
    a = 5
    def func1(x):
        print(m + a + x)
        #m + a = 14

    return func1

#func1引用了func的m 和 a
#然后func将func1的结果进行返回

res = func(9)

res(3)#17



def fun1(name,cls):

    def fung(x):
        if(int(x)>=18):

            print("{}{}班够岁数了".format(name,cls))
        else:
            print("{}{}班NO够岁数了".format(name,cls))

    return fung

res1 = fun1('陈','10')
res1(19)


