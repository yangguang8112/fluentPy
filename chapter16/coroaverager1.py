"""
用于计算移动平均值的协程
>>> coro_avg = averager()
>>> from inspect import getgeneratorstate
>>> getgeneratorstate(coro_avg)
'GEN_SUSPENDED'
>>> coro_avg.send(10)
10.0
>>> coro_avg.send(30)
20.0
>>> coro_avg.send(5)
15.0
"""


from coroutine import coroutine

@coroutine
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count