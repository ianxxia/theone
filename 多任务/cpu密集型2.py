
import  multiprocessing
import threading

def random():
    num = 0
    for i in range(50000000):
        num += 1

def main():
    import time
    t1 = time.time()
    for i in range(4):
        random()
    t2 = time.time()

    t1=t2-t1
    print(t1)


if __name__ == '__main__':
    main()
