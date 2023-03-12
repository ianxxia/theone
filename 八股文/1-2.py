l2 = []

a = {'num':0}

for i in range(3):
#[{'num': 2}, {'num': 2}, {'num': 2}]
#字典是可变的 会同时把列表里面的字典也一起修改了
#所有内存里a的变量会同时修改


    a['num']  = i
    l2.append(a)

print(l2)

#并集
