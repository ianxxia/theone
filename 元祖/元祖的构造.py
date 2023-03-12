#一组有序不可变
list = [1,2,3,4,5,6]
tuple1 = (1,2,3,4,5)

a= ("haahhaah")
print(type(a))#str
b = ("ahdjsad",)
print(type(b))#tuple

tup2 = 1,2,3,4,5
print(type(tup2))#tuple

print(tuple(list)) #转换
print(tuple('hhhhaa'))

dict1 = {'name':'tom','age':'12','sex':'girl'}

print(tuple(dict1))#('name', 'age', 'sex') 只有key

print(tuple(range(10)))#(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

#元祖可以嵌套元祖
