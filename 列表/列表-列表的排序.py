
list1 = ['py','ja','cpp']
list2 = ['py','ja','cpp','vvv','www','e','s']
list3 = ['a','c','d','t','P','Q']

list4 = [-1,-4,-99,-7879,-235,88]
print(sorted(list2))
#大写字母A-Z 再到 小写字母a-z的顺序排序
#不会改变原有列表的顺序
print(sorted(list2, reverse=True))
print(list2)
#跟sorted相反的顺序
list3.sort()
print(list3)
#sort会改变列表内容 sorted不会改变
print(sorted(list4, key=abs))#[-1, -4, 88, -99, -235, -7879]

