dict1 = {'name' : 'tom','age':'15','sex':'楠'}

dict2 = {'name' : 't','age':'15','sex':'楠','add':'sdsd'}

print(dict2.get('age'))
print(dict2['age'])
print(dict1.get('aaa','不存在啊欧美'))
print(dict1.setdefault('age1','no'))#key不存在 返回no

print(dict2.keys())
print(dict2.values())
print(dict2.items())

k = dict1.keys()
l = list(k)
print(l)