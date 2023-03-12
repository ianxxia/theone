set1 = {'name',19,'kk'}

# set1.add('aaa')
# print(set1)

# set1.remove('python1')
# print(set1)

set1.discard('python1') #当参数不存在的时候 返回原集合
print(set1)

# set1.pop() #随机删除
# print(set1)
#
# set1.clear()

# del set1 #从内存角度删除集合NameError: name 'set1' is not defined
# print(set1)

# for i in set1:
#     print(i)

#迭代器
its = iter(set1) #将set1变成可迭代
print(next(its))