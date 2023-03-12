import threading
import time


def car1(n):
    for i in range(20):
        print(n+'已接送{}个学生'.format(10+10*i))
        time.sleep(1)

def car2(num):
    for i in range(20):
        print(num + '已接送{}个学生'.format(10+10*i))
        time.sleep(1)


def main():

    t1 = threading.Thread(target=car1,args=('第一辆车',))
    t2 = threading.Thread(target=car2,kwargs={'num':'第二辆车'})
    t2.start()
    t1.start()

if __name__ == '__main__':
    main()

