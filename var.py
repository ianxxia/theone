
#整形转换浮点型
print(int(1.999))
print(float(22))

#整形---字符串
#int----str
print(int('1234'))
print(int('-1234'))

#
str = 'chenxian'
print(str[-1])
print(str[0:4]) #==print(str[:4])
print(str[:4])
#不包含4
#从第二个字符到最后一个
print(str[2:])
#从第二个字符开始到倒数第一个
print(str[2:-1])
#从开头到最后
print(str[:-1])

#chenxian
#步长间隔
str1='chenxianchen'
print('===================')
print(str1[2:-1:2])
print('===================')
print(str1[10:2:-2])
#步长为负数代表反方向
print(str1[2:7:2])
#长度len内件方法
#count类方法用.调用,计算入参字符串个数
print(len(str1))
print(str1.count('chen'))
#从str1字符串的2到9之间查找有多少个chen
print(str1.count("chen", 2, 9))

print(str1.count('chen', 0, len(str1)))
#-1不包含最后一个字符
print(str1.count('chen',0,-1))
#find()第一次出现的下标 没有查找到返回-1
print(str1.find('hen'))

#rfind()返回字符串右往左数 最后一次出现的位置，如果没有匹配项则返回-1。chenxianchen
print(str1.rfind('chen'))
#index()索引值
print(str1.index('hen'))
#eval可以将字符串表达式计算并转换为int
print(eval('1234'))

#capitalize将字符串首字母变成大写

print(str1.capitalize())
#title每个首字母大写
str3='chEn xian'
print(str3.title())
print(str3.lower())
print(str3.upper())
#swapcase 字符串大小写互换
print(str3.swapcase())

str1='abcdcba'
middle = int(len(str1)/2)
max = int(len(str1))
print(middle)
print(max)
print(str1[(max-1):(middle-1):-1])