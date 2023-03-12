
import re

t = "2022-09-24"

print(re.match('2022-09-24','2022-09-24'))

print(re.match('\d{4}-\d{2}-\d{2}', '2021-09-24'))

print(re.match('\d{4}-0[1-9]-\d{2}','2022-13-28'))

print(re.match('\d{4}-(0[1-9]|[0-2])-([0-2]\d|[3][0-1])',t))
print(re.match('\d{4}-(0[1-9]|[0-2])-([0-2]\d|[3][0-1])',t).group(0))
print(re.match('\d{4}-(0[1-9]|[0-2])-([0-2]\d|[3][0-1])',t).group(1))
print(re.match('(\d{4})-(0[1-9]|[0-2])-([0-2]\d|[3][0-1])',t).group(2))
#以（）为分组 group（1） 2 3分组


con = '''<title> this is python3 <title>'''

print(re.match(r'<title>([\w\W]*)<title>',con).group(1))
# this is python3

print(re.match(r'<(\w+)>([\w\W]*)<\1>',con).group(1))
#\1代表使用第一个分组的正则表达式

#别名(?P<name>) 引用别名(?P=name)

print(re.match(r'<(?P<tag>\w+)>([\w\W]*)<(?P=tag)>',con).group(1))


