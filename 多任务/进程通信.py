import time

import multiprocessing


def sm(name,se):

    time.sleep(2)
    se.put(name)
    print('{}已发送'.format(name))
    print(id(se),'se函数内')


def main():

    send_email = multiprocessing.Queue(5)
    p = ['线路一','线路二']
    print(id(send_email),'main函数内')
    for i in p :
        b = multiprocessing.Process(target=sm,args=(i,send_email))
        b.start()
    time.sleep(4)
    while not send_email.empty():
        print('一共发送',send_email.get())#如果是空的会一直处于阻塞状态


if __name__ == '__main__':
    main()