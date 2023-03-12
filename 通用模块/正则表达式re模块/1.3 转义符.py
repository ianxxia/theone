
import re

'''


'''

str1 = 'c:\\python\ne\test.py'
str2 = r'c\\python\ne\test.py'

print(str1,str2)

print(re.match('\\d', '\d'))
#\\d拼配不出来的原因 \是转义符 \d
print(re.match('\\\d', '\d'))
#<re.Match object; span=(0, 2), match='\\d'>
#python 默认将\d当成路径 \\d

#优先使用python语法 再使用正则表达式处理
print(re.match('\n', '\n'))
#\n在python和正则里面都是换行

print(re.match('\d', '\d')) #\d \\d
print(re.match('\\d', '\d'))#\d  \\d
print(re.match('\\\d', '\d'))#\\d  \\d
print(re.match('\\\\d', '\d'))#\\d  \\d
#第四个\转义\ \转义\ 所有是\\d



