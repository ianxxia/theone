dict1 = {'name' : 'tom','age':'15','sex':'楠'}

dict2 = {'name' : 'tom','age':'15','sex':'楠'}

# del dict1
#print(dict1)#NameError: name 'dict1' is not defined
del dict1['sex']
print(dict1)

#pop()
res = dict1.pop('age','删除了哈哈')
print(dict1,res)

res1 = dict1.pop('agse','删除了哈哈')
print(dict1,res1)#当要删除的key不存在的时候 返回第二个参数

res2 = dict1.popitem()
print(dict2,res2)#{'name': 'tom', 'age': '15', 'sex': '楠'} ('name', 'tom')

#clear() 清空字典
dict1.clear()
print(dict1)