num1=10
num2=20
num3=30
num4=40

max = num1 if num1 > num2 else num2
print(max)

max2 = num1 if num1 > num2 else num3 if num3 > num4 else num4
print(max2)