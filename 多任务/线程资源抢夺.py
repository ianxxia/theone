import threading
import time

ok_num = 0
def car1(lock):
    global ok_num
    for i in range(1000000):
        lock.acquire()
        ok_num  += 1
        lock.release()
    print(ok_num)


def car2(num):
    global ok_num
    for i in range(1000000):
        num.acquire()
        ok_num  -= 1
        num.release()
    print(ok_num)


def main():
    lock = threading.Lock()

    t1 = threading.Thread(target=car1,args=(lock,))
    t2 = threading.Thread(target=car2,kwargs={'num':lock})
    t1.daemon = True

    t1.start()
    t2.daemon = True

    t2.start()

    time.sleep(6)
    print('#######')
    print(ok_num)

if __name__ == '__main__':
    main()

