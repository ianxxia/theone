
'''
求两个集合的交集  并集和差集 说明结果
set1 = {2,2.2,True.4+3j}
set2  = {1,2.2,False,4+3j}


'''

set1 = {2,2.2,True,4+3j}
set2  = {1,2.2,False,4+3j}

print(set1 & set2)

print(set2 & set1)
#以第二个集合为优先级
#1 == True
