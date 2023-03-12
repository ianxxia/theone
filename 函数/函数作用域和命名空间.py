a = 100#全局变量

def func():
    b = 50
    global a
    '''
    函数内将a设置为全局变量 并且重新赋值
    '''

    a =99

    print('函数内ac',a,id(a))
    print('函数内bc',b,id(b))

    def funcc():

        print('函数内acc',a,id(a))
        print('函数内bcc',b,id(b))
    funcc()

'''
全局变量 a
func1（）
    func1变量b
    func1能引用a不能引用c
    func2（）
        func2变量c
        func2能引用a和b
'''


print('函数外a',a,id(a))
func()
print('函数外a',a,id(a))