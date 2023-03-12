import datetime

t = datetime.datetime.now()#已格式化的时间 且符合时区
print(t)#2023-01-29 16:41:18.824746

print(datetime.datetime.today())#不按照时区

print(datetime.datetime(2018, 9, 11, 00, 38, 0))
#2018-09-11 00:38:00 将一组整形数据 格式化为字符串

print(t.strftime('%Y-%m-%d %X'))
#2023-01-29 16:44:19

#两个时间的时间差
t1 = datetime.datetime(1986,9,4)
t2 = datetime.datetime(2021,9,17)
print(t1)
print(t2-t1)#12797 days, 0:00:00
print((t2-t1).total_seconds())#转为秒

print(t + datetime.timedelta(days=13))
#2023-02-11 16:53:14.766647