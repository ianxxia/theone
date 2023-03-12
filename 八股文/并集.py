

'''
求两个集合的交集  并集和差集 说明结果
set1 = {2,2.2,True.4+3j}
set2  = {1,2.2,False,4+3j}


'''

set1 = {2,2.2,True,4+3j}
set2  = {1,2.2,False,4+3j}

print(set1 | set2)
#先展示第一个参数的元素
#1和True是一样 所以把1当做True的相同元素去看 不输出
print(set2 | set1)
#先展示第一个参数的元素
#1和True是一样 所以把True当做1的相同元素去看 不输出

print(set1 - set2)

print(set2 - set1)