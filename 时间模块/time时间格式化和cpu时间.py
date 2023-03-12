

import  time

res = time.time()
print(res)

print(time.ctime(res))#Sat Jan 28 22:35:23 2023

print(time.asctime(time.localtime()))#时间元祖转换为字符串

print(time.strftime('%y-%m-%d %H:%M:%S', time.localtime()))
#23-01-28 22:48:34

print(time.strptime('23-01-28 22:48:34','%y-%m-%d %H:%M:%S'))

#clock() python 3.8之前使用该方法获取cpu时间
#perf_counter python3.8之后使用

t1 = time.perf_counter()
for i in range(10000):
    print(i)


t2 = time.perf_counter()
print(t2 - t1)#0.0607338

