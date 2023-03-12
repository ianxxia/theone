import threading
import time

ok_num = []
def car1(n):
    for i in range(20):
        print(n+'已接送{}个学生'.format(10+10*i))
        time.sleep(1)
        ok_num.append(10+10*i)

def car2(num):
    for i in range(20):
        print(num + '已接送{}个学生'.format(10+10*i))
        time.sleep(1)
        ok_num.append(10+10*i)


def main():

    t1 = threading.Thread(target=car1,args=('第一辆车',))
    t2 = threading.Thread(target=car2,kwargs={'num':'第二辆车'})
    t1.daemon = True

    t1.start()
    t2.daemon = True

    t2.start()

    time.sleep(6)
    print('#######')
    print(ok_num)

if __name__ == '__main__':
    main()

