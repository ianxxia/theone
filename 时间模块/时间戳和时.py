

import time

res = time.time()#时间戳
print(res)

t = time.gmtime(res)#转时间元祖
print(t)
#time.struct_time(tm_year=2023, tm_mon=1, tm_mday=28, tm_hour=10, tm_min=19, tm_sec=55, tm_wday=5, tm_yday=28, tm_isdst=0)

bt = time.localtime(res)#本地时间 时间元祖
print(bt,'localtime')

print(time.mktime(bt))#1674901861.0
