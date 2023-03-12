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
    t1 = threading.Thread(target=car1)
    t2 = threading.Thread(target=car2)
    t1.start()
    t2.start()

if __name__ == '__main__':
    main()

