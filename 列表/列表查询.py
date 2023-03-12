
list1 = ['py','ja','cpp']
list2 = ['py','ja','cpp','cpp','vvv','www','e','s']

#直接查找
print(list1[0])
print(list1[-2])


#index()
print(list2.index('cpp'))
print(list2.index('cpp', 0,3))#在列表0-2长度内查找入参是否存在 开区间


#count()查找元素出现的次数
print(list2.count('cpp'))

#切片操作[start:end:step]
print(list2[1:5:2])

#遍历
list3 = ['py','ja','cpp','cpp','vvv','www']
a=0
print('*'*50)
for i in list3:
    print(i)
    # print(list3.index(i))#返回下标 两个CPP的下标一样 cpp 2 cpp 2
    print(list3.index(i,a))
    a+=1
#index()返回第一个符合元素的下标记

for i in range(0,len(list3)):#不包含最大值 开区间
    print(i)

#枚举
print(enumerate(list3))
#输出<enumerate object at 0x000001B1CE121FC0>可以转回列表
print(list(enumerate(list3)))
#输出 元祖 [(0, 'py'), (1, 'ja'), (2, 'cpp'), (3, 'cpp'), (4, 'vvv'), (5, 'www')]
#
print(list(enumerate(list3, 3)))
#参数2 下标开始的位置


for k,v in enumerate(list3):
    print(k,v)

