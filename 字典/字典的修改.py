dict1 = {'name' : 'tom','age':'15','sex':'楠'}

dict2 = {'name' : 't','age':'15','sex':'楠','add':'sdsd'}

# dict1['name'] ='jj'#若没有key name则为新增 若有则为修改

dict2.update(dict1)#key相同修改值 key没有则新增在后面
print(dict2)