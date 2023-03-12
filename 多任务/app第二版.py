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

def cook_food(food,fl):
        print('{}已开始处理'.format(food))
        time.sleep(2)
        print('{}已完成制作可以上菜'.format(food))
        fl.append(food)


# def send_food(menu):
#
#         sf = menu.get()
#         time.sleep(2)
#         print('您点的{}已送到'.format(sf))


def main():

    book_list = ['鱼','肉','菜']
    manage = multiprocessing.Manager()
    food_list = manage.list()
    # food_list = manage.dict()
    # food_list = manage.Value()


    for i in book_list:
        book_food = multiprocessing.Process(target=cook_food,args=(i,food_list))
        book_food.start()
    time.sleep(3)
    print(food_list)

if __name__ == '__main__':
    main()




