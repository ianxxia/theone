import multiprocessing
import threading

def random():
    num = 0
    while True:
        num += 1

def main():

    import os
    cpus = os.cpu_count()
    print(cpus)
    m = multiprocessing.Process()
    t = threading.Thread
    for i in range(cpus):
        tol = m(target = random())
        tol.start()


if __name__ =='__main__':
    main()