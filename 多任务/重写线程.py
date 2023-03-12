import threading
import time


class My_Thread1(threading.Thread):
    def run(self):

        for  i in range(5):
            self.func()
            print('第一辆车已经送了%d' % (10 + 10 * i))
            time.sleep(1)
    def func(self):
        print('######'*2)

class My_Thread2(threading.Thread):
    def run(self):
        for  i in range(5):
            print('第二辆车已经送了%d' % (10 + 10 * i))
            time.sleep(1)

def main():
    mt1 = My_Thread1()
    mt1.start()
    mt2 = My_Thread2()
    mt2.start()


if __name__ == '__main__':
    main()

