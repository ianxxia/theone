import calendar

# print(calendar.month(2021, 9,w=2,l=3))

'''   September 2021
Mo Tu We Th Fr Sa Su
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30

l为上下间隔'''

print(calendar.calendar(2021,w=5,l=1,c=5))#输出一年的日历
#第二个参数是影响格式 c是每个月横向间隔

print(calendar.firstweekday())#首次加载 0代表星期一

print(calendar.isleap(2021))#判断是否闰年

print(calendar.leapdays(1999, 2203))

print(calendar.monthcalendar(2021, 9))
#用列表表示月历
l = calendar.monthcalendar(2022,9)

print(l[1][2])

print(calendar.monthcalendar(2021, 8))

print(calendar.prcal(2021, w=2, l=1, c=5))

import time
res = time.localtime(time.time())
print(calendar.timegm(res))#将时间元祖改成时间戳





