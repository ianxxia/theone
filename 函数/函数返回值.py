
def fun1(a,b):
    print('返回')
    return a+b
    print('retun之后的语句都不执行')


a=fun1(3,5)
print(a)

def func(a,b):
    '''求和求差的函数'''
    res1 = a+b
    res2 = a-b
    return (res1,res2)#<class 'tuple'>

res = func(3,5)[1]
print(res)

help(func)#输出帮助文档
#func(a, b)
#求和求差的函数
#