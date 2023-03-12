#break   终止循环体
#continue 结束本次循环 跳到下次循环
#pass     占位作用


def fun1():
    pass

i=0
while True:
    print(i)
    i+=1
    if i == 10:
        break

while True:

    i+=1
    if i == 10:
        continue
    if i ==15:
        break
    print(i)

