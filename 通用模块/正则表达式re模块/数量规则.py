
import re

#匹配 13898761234

print(re.match('\d*', '13898761234'))#贪婪模式
#* 匹配前一个字符出现的任意次数
print(re.match('\d*', 'a13898761234'))
#<re.Match object; span=(0, 0), match=''>
print(re.match('\d*', '13898761a234'))
#<re.Match object; span=(0, 8), match='13898761'>

#+
print(re.match('\w+', '138987a61234'))
#只要出现一次就符合 <re.Match object; span=(0, 12), match='138987a61234'>
print(re.match('\d+', '138987a61234'))

#?
print(re.match('\d?', '138987a61234'))
print(re.match('\d?', 'a'))
print(re.match('\d?', ''))


#{m} {m,} {m,n}
print(re.match('\d{3}', '138987a61234'))
#<re.Match object; span=(0, 3), match='138'>
print(re.match('\d{3,}', '138987a61234'))
#<re.Match object; span=(0, 6), match='138987'>
#至少出现三次 上不封顶 贪婪模式
print(re.match('\d{3,5}', '138987a61234'))
#至少出现3-5次之间
