
# def numbers():
#     i = 0
#     while True:
#         ret = yield f'{i: b}'
#         i += ret


from concurrent import futures
import threading
from arcfour import arcfour
from arcfour_futures import arcfour_test, KEY, SIZE
import time


def ceshirun(num):
    while True:
        pass
        # print(num)

def run_futures(threads_num=2):
    with futures.ThreadPoolExecutor(max_workers=threads_num) as executor:
        res = executor.map(ceshirun, range(threads_num))

def run_threads2(threads_nums=2):
    for i in range(threads_nums):
        thread = threading.Thread(target=ceshirun, args=[i])
        thread.start()
    
    for t in threading.enumerate():
        if t != threading.current_thread():
            t.join()
    
    print("done")


def run_threads(threads_num=2):
    for i in range(threads_num, 0, -1):
        size = SIZE + int(SIZE / threads_num * (i - threads_num/2))
        thread = threading.Thread(target=arcfour_test, name='t{i}', args=[size, KEY])
        thread.start()

    for t in threading.enumerate():
        if t != threading.current_thread():
            t.join()
    # 主线程继续执行
    print("Done.")
    


run_threads2()

# 总结：python的多线程确实不行，就算死循环，打印的和c差太远了，所有的线程突破不了一个核的资源（GIL）