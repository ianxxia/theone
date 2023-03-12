

'''
%d 数字
%s 字符
%f 浮点型
%3.f 小数点后三位 自动四舍五入

\n 换行
\r 回车
\t 缩进 4个空格 制表符
\  续航符号

\ 转义符
r 转义多个字符

'''
int1=100
print('%d个月精通C++' % (int1))
#\续航符
str = 'chen\n,xian\r hah\thh' \
      'hh'
print(str)
#\转义符
str2 = 'D:\\root\\ruser'
str3 = r'D:\root\ruser'
print(str3)

a=input('输入a  ')
b=input('输入b  ')
a=int(a)
b=int(b)
c=b-a
# print(type(c))
for i in range(c) :
      print(a+i)





