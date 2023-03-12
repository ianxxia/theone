'''
线程切换的原理和时机
1.执行完成一定量的字节数会切换
执行一定时间跨度后切换
碰到io操作后切换
遇到主动等待后切换

线程切换和调度资源开销大 以上的切换都不是智能切换
时机把握恨不准确  所以引入协程来手动智能切换线程


协程优势
多个协程共享同一个线程中的资源 仅仅只有自己独立的寄存器和
栈 创建协程开销比线程更小

携程之间的切换是程序级别 进程和线程都是操作系统级别
不会出现资源冲突 就不需要线程锁参与  提高效率


'''

import time
import gevent

t=0
t1=0
t2=0
def run1():
    print('run1开始')
    gevent.sleep(2)
    print('run1结束')
    global t1
    t1 = time.perf_counter()
    print(t1)

def run2():
    print('run2开始')
    gevent.sleep(2)
    print('run2结束')
    global t2
    t2 =t1+ time.perf_counter()
def main():
    g1 = gevent.spawn(run1)
    g2 = gevent.spawn(run2)
    # run1()
    # run2()

    gevent.joinall([g1,g2])

    print(t2)



if __name__ == '__main__':
    main()


