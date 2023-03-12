import threading
import time


class My_Thread1(threading.Thread):
    def __init__(self,n):
        super().__init__()
        self.n = n
    def run(self):

        for  i in range(5):

            print('{}已经送了{}'.format(self.n,(10+10 * i)))
            time.sleep(1)


class My_Thread2(threading.Thread):
    def __init__(self,n):
        super().__init__()
        self.n = n

    def run(self):
        for  i in range(5):
            print('{}已经送了{}'.format(self.n,(10+10 * i)))
            time.sleep(1)

def main():
    mt1 = My_Thread1('第一辆车')
    mt1.start()
    mt2 = My_Thread2('第二辆车')
    mt2.start()


if __name__ == '__main__':
    main()

