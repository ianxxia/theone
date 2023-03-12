


#1.函数装饰器
# def check(func):
#     def test():
#         print('身份验证')
#         func()
#
#     return test
#
# @check
# def load():
#     print('登录成功')

# load()

#__call__
class Check:
    def __init__(self,func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('身份验证')
        self.func()
@Check
def load():
    print('登录成功')

load()


