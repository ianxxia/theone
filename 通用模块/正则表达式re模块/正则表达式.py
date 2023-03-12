
import  re

str = 'abcd'

pattern = 'ab'

res = re.match(pattern,str)
print(res)
#<re.Match object; span=(0, 2), match='ab'>
print(res.group())#ab

print(re.findall(pattern, str))
#['ab'] 列表 str里面能匹配到的都输出
