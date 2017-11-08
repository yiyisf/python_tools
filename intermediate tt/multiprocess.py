"""
多线程
"""
import multiprocessing


def spawn(num, num1) :
    print("Spawned #{} {}".format(num, num1))

if __name__ == '__main__':
    for i in range(10):
        p = multiprocessing.Process(target= spawn, args=(i, i+1))
        p.start()
        # p.join()