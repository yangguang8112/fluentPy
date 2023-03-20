from concurrent import futures
from tqdm import tqdm


def ceshirun():
    while True:
        pass


with futures.ThreadPoolExecutor(max_workers=5) as executor:
    to_do = []
    for _ in range(5):
        future = executor.submit(ceshirun())
        to_do.append(future)
    done_iter = futures.as_completed(to_do)
    done_iter = tqdm(done_iter, total=10000)
    for index, future in enumerate(done_iter):
        pass

