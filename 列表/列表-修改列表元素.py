#直接修改
list1 = ['py','ja','cpp']
list2 = ['py','ja','cpp','vvv','www','e','s']

list2[2]='java'
print(list2)

list2[0:3] = ['1','2','3']
print(list2)

num = [1,2,3,4,7,5,787,9,64,5,4,2,7,8]
num.sort() #从小到大排列
print(num)
list3 = ['py','ja','cpp','vvv','www','e','s']
list3.sort()
print(list3)
#ASCII
num.reverse()  #反转地球 翻转排列
print(num)

import random #内置库
random.shuffle(num) #随机排列 打乱顺序
print(num)