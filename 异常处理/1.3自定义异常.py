


#方法二

# try:
# test(8,0)
# except ZeroDivisionError:
#     print('除数不能为0啊啊啊')
print('代码到这里了')

class ZeroErr(BaseException):
    def __init__(self,msg):
        self.msg=msg

def test(m,n):
    if n == 0:
        print('除数不能为0')
        raise ZeroErr('除数不能为0啊啊啊')#抛出异常后不会继续执行
    else:
        print(m/n)

test(8,0)
