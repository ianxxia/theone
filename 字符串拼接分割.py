

str1 = '2022-1-23-23:00'
#用指定的字符分割字符串，返回以列表格式
print(str1.split('-',2)) #第二个参数是分隔的次数
#partition返回一个元祖
#返回第一次出现分隔符的左边，右边，和剩下的
# print(str1.partition('-'))
# print(str1.rpartition('-'))
str3 = ['chen','xian','a','hh']
print('-'.join(str3))
#字符串和列表都可以进行join拼接