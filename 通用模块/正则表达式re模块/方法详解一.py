
import re


content = '''<title>this is python<title>'''

res = re.compile(r'<title>([\w\W]*)<title>')

print(res.match(content))

res1 = re.compile('aa',flags=re.I)
#忽略大小写
print(res1.match('Aa'))
#<re.Match object; span=(0, 2), match='Aa'>
'''
flags = re.S #点的任意匹配模式 改变'.'的行为
re.L 使预定字符类 \w \W \b \B \s \S 取决于当前区域设定
re.M 多行模式 改变^ $
re.X 详细模式 这个模式下正则可以是多行 忽略空白
re.U 使预定字符类 \w \W \b \B \s \S \d \D 取决于unicode的字符属性

'''