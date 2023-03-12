
print('我是%s班' % 2)
print('我是{}班'.format(2))

def newstu(name,cla):
    print('我叫{},我是{}班'.format(name,cla))

import functools
new1 = functools.partial(newstu,cla=2)#放入参数名 和偏好的入参值

new1(name='cx')#我叫cx,我是2班

