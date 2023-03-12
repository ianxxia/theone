import threading
import time


def car1():
    for i in range(20):
        print('已接送{}个学生'.format(10+10*i))
        time.sleep(1)

def car2():
    for i in range(20):
        print('已接送{}个学生'.format(10+10*i))
        time.sleep(1)


def main():

    t1 = threading.Thread()
    t1.run= car1()#把函数赋值给run
    t1.start()

if __name__ == '__main__':
    main()

