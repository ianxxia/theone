
set1 = {'name',19,'kk'}
#无序的无法通过下标访问 没有键也不能通过键访问 所以集合无法查询访问
#可变集合（set） 可以进行增删改查
#不可变集合（frozenset） 创建好之后无法增删改查 只能查询

#集合是一种无序 不重复且不可随机访问的元素集合

set2 = set('sdsd')
print(set2) #{'s', 'd'}无序不重复的元素
dict1={'s':'kei','vv':'33'}
set3 = set(dict1)
print(set3) #只输出key{'s', 'vv'}

set4 = {i for i in range(5)}
print(set4)

set5 = frozenset(set2)
print(set5)

set6 = {} #默认为dict类型
set7 = set() #<class 'set'>
set8 = frozenset() # <class 'frozenset'>
print(type(set7),type(set8))

