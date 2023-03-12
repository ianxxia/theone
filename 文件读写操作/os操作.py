import os

#1重命名文件
#os.rename('abc.txt','abcd.txt')
#os.renames('../aaa/abc.txt','../acc/abcd.txt')
#renames 以树状的形式 能修改文件的路径


# os.remove('../acc/abcd.txt')
# os.rmdir('../acc/acb')#不能删除非空目录
# os.removedirs()#第一个目录后的路径全部删除
# #例如 f/t/q
#rmdir 会删除q
#removedirs 会删除t/q

# os.mkdir('../acc/acd')

#获取当前目录
# print(os.getcwd())
#
# os.chdir('../aaa')
#
# print(os.getcwd())

#获取目录下的内容列表
print(os.listdir(os.getcwd()))
#返回列表
#['os操作.py', '文件定位.py', '文件操作-文件读写和关闭操作.py', '文件读写操作1.py']