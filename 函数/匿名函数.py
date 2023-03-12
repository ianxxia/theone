#匿名函数是没有函数名的函数 有返回值
#表达式的结果就是返回值 不能写return
#一半用于简单的函数处理

#lambda 形参1 形参2 ：表达式

#(lambda 形参1，形参2，...：表达式)（实参1，实参2）

res = lambda m, n: m + n
print(type(res))#<class 'function'>

print(res(3, 6))#9

print((lambda a,b:a * b)(6,3))


list1 = [{'name':'T','age':'16'},{'name':'T2','age':'19'},{'name':'ds','age':'14'}]

res1 = sorted(list1,key=lambda x:x['age'])

print(res1)

res2 = (lambda name,cls:print('我是{},我是{}班'.format(name,cls)))

res2('abin',3)
