
#无序可变的数据类型
dict1 = {'name' : 'tom','age':'15','sex':'楠'}

print(type(dict1))
#key不能重复
#key 不可变的数据类型 列表不能当作key

#类型转换
#dict()
demo1 = [('name','tom'),('age','18'),('sex','楠')]

print(dict(demo1))#{'name': 'tom', 'age': '18', 'sex': '楠'}

keys = [1,2,3]
values=['ss','ee','cc']
print(dict(zip(keys,values)))#{1: 'ss', 2: 'ee', 3: 'cc'}

dict1['aaa'] = 11 #追加{'name': 'tom', 'age': '15', 'sex': '楠', 'aaa': 11}
print(dict1)