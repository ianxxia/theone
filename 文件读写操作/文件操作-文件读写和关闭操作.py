

f = open('../aaa/abc.txt','r',encoding="utf-8")
res = f.readline()
res2 = f.readlines()
print(res)
print(res2)

import collections.abc
print(isinstance(f,collections.abc.Iterator))

for i in res2:
    print(i,end='')

f.close()
f.flush()
