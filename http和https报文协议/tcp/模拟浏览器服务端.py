import socket
#创建会话对象
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#固定格式 流数据

#建立连接
server.bind(('192.168.31.109',8001))

#设置监听
server.listen(5)
print('##########')


#阻塞连接
info,addr = server.accept()
print('#######2')


while True:
    data = info.recv(1024)
    print('收到客户端信息'+ data.decode('utf-8'))
    send_data = input('请返回数据给客户端')
    info.send(send_data.encode('utf-8'))

    pass
