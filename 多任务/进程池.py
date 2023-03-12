'''
点菜app
1.客户点菜之后交给厨师做菜

2.厨师做好的菜交给服务员上菜
'''

#任务是什么 点菜
#任务是由谁发出 客户
#任务的流程 客户点菜 厨师做菜 服务员上菜

import time
import multiprocessing

def cook_food(num,lock):
    for i in range(500):
        lock.acquire()#加锁 资源变动之前
        num['count'] += 1
        lock.release()#解锁
    print('进程结束 ',num['count'])




# def send_food(menu):
#
#         sf = menu.get()
#         time.sleep(2)
#         print('您点的{}已送到'.format(sf))


def main():


    manage = multiprocessing.Manager()
    md = manage.dict()
    md['count'] = 0

    # food_list = manage.dict()
    # food_list = manage.Value()

    lock = multiprocessing.Manager().Lock()
    pool = multiprocessing.Pool(10)
    for i in range(15):
        pool.apply_async(func=cook_food,args=(md,lock))
#async是并联的
#apply 是串联
    # time.sleep(3)
    # print(md)
    pool.close()
    pool.join()


if __name__ == '__main__':
    main()




