import re

#13898761234

tel = '13889038198'

print(re.match('\d*', tel))
#第一位一定1开头
#第二位3 5 8
#第三位135 136 -- 139
#后面还有8位
#$ 结束的意思
print(re.match('^1[358][5-9]\d{8}$', tel))

#单词边界
str1 = 'i put eda lightediwuqed effdeed eoed eddddddiiiiiijuzi'
print(re.findall('ed', str1))
#['ed', 'ed']
#找ed结尾的
#\b边界
#\B非边界
print(re.findall('\w*ed\\b', str1))
# print(re.findall(r'ed\b', str1))
# print(re.findall('\\bed', str1))
#
print(re.findall(r'\b[e][d]\w*', str1))