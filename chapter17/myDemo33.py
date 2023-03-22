
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
        print(num)

def run_futures(threads_num=2):
    with futures.ThreadPoolExecutor(max_workers=threads_num) as executor:
        res = executor.map(ceshirun, range(threads_num))

def run_threads(threads_num=2):
    for i in range(threads_num, 0, -1):
        size = SIZE + int(SIZE / threads_num * (i - threads_num/2))
        thread = threading.Thread(target=arcfour_test, name='t{i}', args=[size, KEY])
        thread.start()
    


run_threads(600)

