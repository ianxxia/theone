'''
while 条件语句:
    代码（满足条件）

'''

i=10
while i>5:
    i -=1
    i= i if i%2==0 else i-2
    print("sjs{}{}".format(i,i%2))



