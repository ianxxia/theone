import socket
#创建会话对象
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#固定格式 流数据

#建立连接
client.connect(('192.168.31.109',8001))


while True:
    data = input('请输入给服务器的信息:')
    client.send(data.encode('utf-8'))
    back_info = client.recv(1024).decode('utf-8')
    print('已收到'+back_info)
    pass
