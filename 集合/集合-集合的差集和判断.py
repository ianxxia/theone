set3 = {1,2,3}
set4 = {1,2}

#差集
#A 123  B 345
#A差集为 12

res = set3.difference(set4)
print(res)

set3.difference_update(set4)
print(set3)

#判断两个集合之间是否不相交
res = set3.isdisjoint(set4)
print(res)

set3 = {1,2,3}
set4 = {1,2,3}

#set4是否完全包含set3里面的所有元素 是否被包含
res = set3.issubset(set4)
print(res)

res1 = set3.issuperset(set4)
print(res1)