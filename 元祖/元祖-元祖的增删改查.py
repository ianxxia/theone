
list = [1,2,3,4,5,6]
tuple1 = (1,2,3,4,5)
tuple2 = (12,23,34,45,56,1,5,9,4,8,7,3,7,7)

#del tuple1[1] #
#print(tuple1) #TypeError: 'tuple' object doesn't support item deletion
#元祖不可变
#元祖的拼接
print(tuple1 + tuple2)#(1, 2, 3, 4, 5, 12, 23, 34, 45, 56)
res = tuple1 + tuple2
print(id(res)) #新内存空间 产生了新元祖res

#元祖查询
print(tuple2[5])
print(tuple2[-2])
print(tuple2[1:5])
print(tuple2[4:])#从4到结尾(包含最后一个)
print(tuple2[:4])#从开头到4（不包含4）

print(tuple2[1:5:2])#从1-5间隔2
print(tuple2[::-1])#翻转元素 倒叙输出
print('*' * 50)
#tuple2 = (12,23,34,45,56,1,5,9,4,8,7,3,7,7)
# print(tuple2[2:5:-1])
print(tuple2[5:2:-1])#(1, 56, 45) 不包含2下标的34
