# del删除列表元素或者列表
list1 = ['py','ja','cpp']
list2 = ['py','ja','cpp','vvv','www','e','s']
del list1[1]

print(list1)
del list2[3:5]
print(list2)
del list2[-2]
print(list2)

#pop()
list3 = ['py','ja','cpp']
list4 = ['py','ja','ja','cpp','vvv','www','e','s']

list3.pop(2)
print(list3)
list3.pop()#没有入参指定删除最后一个
print(list3)

#remove() 通过指定元素删除
list4.remove('ja') #删除从左往右第一个ja
print(list4)

#clear()清空元素 变成空的[]空列表

list3.clear()
print(list3)