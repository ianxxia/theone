set1 = {'name',19,'kk'}
set2 = {'name',19,'kk','jj'}

res = set1.intersection(set2) #取交集赋值到一个新集合
print(res)

set3 = {'name',19,'kk'}
set4 = frozenset({'name',19,'kk','jj'})
res1 = set3.intersection(set4)
print(res1,type(res1))#{'name', 19, 'kk'} <class 'set'>

res2 = set4.intersection(set3)
print(res2,type(res2))#frozenset({'name', 19, 'kk'}) <class 'frozenset'>

set5=set3 & set4 #交集
print(set5)
print(type(set5)) #<class 'set'>



#已第一个集合的类型为基准

set3 = {'name',19,'kk','ll'}
set4 = frozenset({'name',19,'kk','jj'})

res3 = set3.intersection_update(set4)
print(res3) #None
print(set3)#{19, 'name', 'kk'}将两个集合的交集赋值


set6=set4 & set3 #交集
print('交集',set6)
# print(type(set6)) #<class 'frozenset'>

set6=set4 | set3 #并集
print('并集',set6)
# print(type(set6)) #<class 'frozenset'>


s1 = {'name',19,'kk'}
s2 = {'name',19,'kk','jj'}

res = set4.union(set3)#并集
print(res)

set3 = {'name',19,'kk','ll'}
set4 = frozenset({'name',19,'kk','jj'})

set3.update(set4)
res = set3.update(set4) #黄色波浪线代表没有返回值
print(set3)
