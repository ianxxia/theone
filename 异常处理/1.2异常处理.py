age = 18

try:
    print(age1) #变量值不存在
# except NameError:
# except ZeroDivisionError as zd:
#将除零错误命名为zd

except (NameError,ZeroDivisionError,IndexError):
    print('变量值age1不存在')

else:
    print('xxxxxx')#当print（age）时输出
finally:
    print("无论什么结果都输出")
#同时存在多个except的时候遇到第一个except

