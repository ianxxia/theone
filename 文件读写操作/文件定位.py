'''



'''
f = open('../aaa/abc.txt','r+',encoding="utf-8")
# f.seek(3)
print(f.read())
f.seek(3)
print(f.tell())#文件偏移的字符个数 非下标
f.seek(3,0)#第二个参数使用0 将文件光标移动回最开头
#0只能用于文本文件
# 1代表开头 2代表结尾 用于二进制文件
f.seek(-3,1)#向左偏移
