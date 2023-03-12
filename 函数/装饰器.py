#通过一段代码给函数加上另一个功能
def check(f):
    def test():
        print('身份认证 ')
        f()
    # return test

@check
def dog():
    print('函数1')
# dog1 = check(dog)

@check
def cat():
    print('函数cat')
# cat1 = check(cat)


call = 'dog'

if call == 'dog':

    dog()
else:

    cat()