import time
import threading
from  concurrent.futures import  ThreadPoolExecutor
def car(c):
    for i in range(5):
        print(c + '已送%d人' % (10 + 10 * i))
        time.sleep(2)

def main():
    cars = ['一','二','三','四']
    poool = ThreadPoolExecutor(max_workers=2)#最大线程数为2
    for c in cars:
        # t = threading.Thread(target=car,args=c,)
        # t.start()
        sub = poool.submit(car,c)

if __name__ =='__main__':
    main()