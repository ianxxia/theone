import socket
#创建会话对象
sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#固定格式 流数据

#建立连接
sk.connect(('www.pyqt5.cn',80))

#发送请求
sk.send(b'GET / HTTP/1.1\r\nHost: www.pyqt5.cn\r\nConnection: close\r\n\r\n')

#等待数据
data = []
while True:
    re_data = sk.recv(1024)
    if re_data:
        data.append(re_data)
    else:
        break

data_str = (b''.join(data)).decode('utf-8')

print(data_str)
