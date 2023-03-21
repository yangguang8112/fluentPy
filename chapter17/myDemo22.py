from concurrent import futures
from tqdm import tqdm


def ceshirun(num):
    while True:
        num += 1
        # print(num)

def spwn(threads_num=2):
    with futures.ThreadPoolExecutor(max_workers=threads_num) as executor:
        res = executor.map(ceshirun, range(threads_num))

with futures.ProcessPoolExecutor(max_workers=2) as executor:
    res = executor.map(spwn, [3, 5])

print(res)



# with futures.ThreadPoolExecutor(max_workers=2) as executor:
#     todo = []
#     for i in range(3):
#         future = executor.submit(ceshirun, i)
#         todo.append(future)
#         msg = 'Scheduled for {}: {}'
#         print(msg.format(i, future))
#     results = []
#     for future in futures.as_completed(todo):
#         res = future.result()
#         msg = '{} result: {!r}'
#         print(msg.format(future, res))
#         results.append(res)
#     print(results)

