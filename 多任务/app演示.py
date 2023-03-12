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

def cook_food(foodname,sq):
    while True:
        food = foodname.get()

        print('{}已开始处理'.format(food))
        time.sleep(2)
        print('{}已完成制作可以上菜'.format(food))
        sq.put(food)


def send_food(menu):
    while True:
        sf = menu.get()
        time.sleep(2)
        print('您点的{}已送到'.format(sf))


def main():

    
    book_queue = multiprocessing.Queue(5)
    send_queue = multiprocessing.Queue(5)

    p1 = multiprocessing.Process(target=cook_food,args=(book_queue,send_queue))
    p1.start()
    p2 = multiprocessing.Process(target=send_food,args=(send_queue,))
    p2.start()

    while True:
        food = input('请点菜：')
        book_queue.put(food)

if __name__ == '__main__':
    main()




