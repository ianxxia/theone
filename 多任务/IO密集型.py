from gevent import monkey
import  os
import time
import multiprocessing
import threading
import gevent

f_dir = r'./f-video'
t_dir = r'/t-video'


def test(name,f_dir,t_dir):
    t1 = time.time()
    with open(f_dir + './' + name,'rb') as ff:
        with  open(t_dir + './' + name,'ab') as tf:
            while True:
                con = ff.read(1024)
                if con:
                    tf.write(con)

                else:
                    break
    t2 = time.time()
    print(t2-t1)
def main():
    file_list  = os.listdir(f_dir)
    t1 = time.time()
    for f in file_list:
        th = threading.Thread(target=test,args=(f,f_dir,t_d))
        th.start()
    t2 = time.time()
    print(t2 - t1)

if __name__ == '__main__':
    main()
