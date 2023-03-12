
import random

print(random.random())#0-1直接随机浮点数

random.uniform(2,3)#2-3之间浮点数随机

random.randint(2,10)#2-10之间的整数

print(random.randrange(10, 30, 2))
#两个参数时 输出1-2参数之间的整数
#第三个参数为2时 则步长为2

list1 = ['1','2','sdhka',242,'xianxian',['1','jsdhf']]
print(random.choice(list1))

print(random.shuffle(list1))#将原序列打乱生成新列表