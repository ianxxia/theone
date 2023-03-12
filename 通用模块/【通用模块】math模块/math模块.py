
import math

#欧几里得范数
print(math.hypot(3,4))
'''在 Python 3.8 之前，此方法用于查找直角三角形的斜边：sqrt(x*x + y*y)。

从 Python 3.8 开始，此方法也用于计算欧几里得范数。 对于 n 维情况，假定传递的坐标类似于 (x1, x2, x3, ..., xn)，从原点开始的欧几里得长度由 sqrt(x1*x1 + x2*x2 +x3*x3 .... xn*xn) 计算。'''

print(math.ceil(3.2))#向上取整
#4
print(math.floor(4.9))#向下取整
#4


print(math.copysign(5, -20))
#-5

print(math.fabs(-99))#返回绝对值 浮点型

print(math.factorial(4))#返回阶乘

print(math.fmod(4, 3))#第一个参数 除以第二个参数的余数
#1.0 浮点型

print(math.gcd(10, 3))#最大公约数

print(math.trunc(3.0679))#返回整数部分

print(math.pow(10,3))#次方
#1000
math.sqrt(16)#开方 4