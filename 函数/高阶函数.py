
def func1(a,b):
    return a + b

def func2(a,b):
    return a - b

def func3(m,n,funcx):
    print(funcx(m,n))
#funcx(m,n) == func1(a,b)

func3(3,4,func1)#7

list1 = [{'name':'T','age':'16'},{'name':'T2','age':'19'},{'name':'ds','age':'14'}]

def getkey(li):
    return li['age']



res = sorted(list1,key=getkey)
print(res)
#list1 作为getkey的入参 输出的结果
# 进行sorted的排序输入