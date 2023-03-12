'''
通过文件句柄 给文件开一个入口 ，通过这个 入口 来操作
文件，句柄有不同的功能通过不同的代码实现
比如读写 定位  关闭
文件分类 txt doc html xml 二进制文件 图片视频音频
打开 open('文件','模式')
读写 定位  读/写
关闭
'''

'''
r 只读 默认模式 文件的指针会放在文件开头
    如果文件不存在则报错
w 只写  文件指针放在文件开头  所写入的内容会覆盖已有内容
    文件不存在则自动创建
a 只写的方式  指针在文件的末尾 不会覆盖 文件不存在则 自动创建

f = open('files/a.txt','r')

读写操纵
content =  f.read()
print(content)

f.close

 
'''
f = open('../aaa/abc.txt','r',encoding='utf-8')
#f = open('D:\pyproject\pythonbase\aaa\abc.txt','r')
print(f.read())
f.close()

f = open('../aaa/test1.txt','w',encoding='utf-8')
print(f.write('sdsdsd'))
f.close()

#以二进制格式对文件进行操作
#rb wb ab 图片视频音频
f = open('../aaa/tiger.jpg','rb')
print(f.read())
res = f.read()
f.close()

f=open('../aaa/tiger2.jpg','wb')
content = res[0: len(res)//2]
f.write(content)
f.close()

#增加+号 表示把当前文件以读写模式打开 带上+表示可读可写
