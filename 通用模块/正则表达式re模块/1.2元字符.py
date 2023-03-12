import  re

'''
. 表示任意一个字符 除了\n
\d 表示0-9之间任意一个数字
\D 表示非数字
\s 表示空白字符
\S 表示非空白
\w 大小写字母,数字,下划线
\W 

'''

print(re.match('.', '123'))
#<re.Match object; span=(0, 1), match='1'>

print(re.match('\d', '0978hujdsj'))
#<re.Match object; span=(0, 1), match='0'>
#从左往右
print(re.match('\D', '\nsjadkjaskd'))

print(re.match('\s', ' '))#<re.Match object; span=(0, 1), match=' '>
print(type(re.match('\s', ' ')))
#<class 're.Match'>

print(re.match('\S', 'j'))

print(re.match('\w', '3'))

print(re.match('[abcd]', 'zb'))
print(re.findall('[abcd]', 'zb'))
print(re.match('[a-e]', 'eb'))
print(re.match('[0-9]', '3a'))
print(re.match('[A-Z]', 'F3a'))
print(re.match('[^a-e]', 'fb'))
#^取反
print(re.match('[a-zA-Z]', 'F3a'))
#a-Z范围内

print(re.match('[0-9][0-9]', '55'))
print(re.match('[0-9][a-zA-Z]', '5Z'))
print(re.match('\w\w', '55'))
