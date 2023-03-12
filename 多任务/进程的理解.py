
#每个进程可以开辟多个线程
import os
def car(num):
    for i in range(10):
        print('第{}辆车已经送了{}个学生'.format(num,10+ 10 * i))
        import time
        time.sleep(1)
        print(os.getpid())

# def car(num):
#     for i in range(10):
#         print('第{}辆车已经送了{}个学生'.format(num,10+ 10 * i))
#         import time
#         time.sleep(1)
#         print(os.getpid())


import multiprocessing#引入进程

def main():
    # 创建进程
    c1 = multiprocessing.Process(target=car,name='cara',args=('car1',))
    c2 = multiprocessing.Process(target=car,kwargs={'num':'car2'})
    #开始执行进程
    c1.start()
    c2.start()
    print(os.getpid())
    # os.kill(c1.pid,9)#杀死进程

if __name__ == '__main__':
    main()

