#*args **kwargs

def func(*args):#传入不定长的参数 任何类型的数据
    print(args)
    print(type(args))#<class 'tuple'>


func()
func(1)#(1,)
       #<class 'tuple'>
func(1,'sdsd','%^&')
func([1,2,3,4],('sdjk','sdj','whew'),{'name':'s'})

def fun2(**kwargs):#任意类型的键值对
    print(kwargs)
    print(type(kwargs))

fun2()
'''
{}
<class 'dict'>
'''
fun2(aa=123,cc=333,hd='sje')#{'aa': 123, 'cc': 333, 'hd': 'sje'}
fun2(aa=['ewe','123',4],bb={'name':'hh','ss':18})
