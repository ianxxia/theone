

import  os
#重命名
# os.rename('111.txt', '222.txt')

#os.renames('222.txt', '555.txt')
#重命名 树状形式找文件 能把文件夹也一并修改

#os.remove('222.txt')
#os.remove('')#不能删除目录
#os.rmdir('f/t/q')#只能删除空目录 会把q删除
#os.removedirs('f/t/q')#只能删除空目录 会把t和q一起删除

#os.mkdir('f/t/q')#若没有t文件夹会报错
print(os.getcwd())#获取当前路径

# print(os.chdir('/home/xianchen'))#改变默认目录

print(os.listdir())#['555.txt', 'c', 'os模块.py']
print(os.listdir(os.getcwd()))
print(os.listdir('../'))#['os模块', '【通用模块】math模块', '随机数模块.py']