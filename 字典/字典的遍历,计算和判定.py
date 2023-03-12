dict1 = {'name' : 'tom','age':'15','sex':'楠'}

dict2 = {'name' : 't','age':'15','sex':'楠','add':'sdsd'}

k = dict2.keys()
print(k)

for k  in dict2:
    print(dict2[k])# = dict1.values()


print('age' in dict2) #只能判断key是否在字典

print(len(dict2)) #4 4组键值对
