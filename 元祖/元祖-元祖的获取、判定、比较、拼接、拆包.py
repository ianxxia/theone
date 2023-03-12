tuple2 = (12,23,34,45,56,1,5,9,4,8,7,3,7,7)

#获取元祖中元素出现到个数
print(tuple2.count(7)) #3
print(tuple2.index(7)) # 首个
print(tuple2.index(7,5,12))
print(len(tuple2))
print(min(tuple2))
print(max(tuple2))

print(7 in tuple2)
print(7 not in tuple2)

tuple3=(1,2,3)
tuple4 = (1,2,3,4)
print(tuple4 > tuple3) #先比较首元素再比较长度

a=1
b=2
c=3
tuple5 = (a,b,c)
print(tuple5)
print(tuple5[0],tuple5[1],tuple5[2])

a,b,c = (1,2,3)
c = 11,22,33# <class 'tuple'>
print(a,b,c)
print(c)
print(type(c)) #<class 'tuple'>