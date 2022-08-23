from xml.sax.handler import feature_external_ges
from tqdm import tqdm
from concurrent import futures
import random
import time


with futures.ThreadPoolExecutor(max_workers=50) as executor:
    to_do = []
    for _ in range(10000):
        future = executor.submit(time.sleep, random.randint(1, 11) * 0.01)
        to_do.append(future)
    done_iter = futures.as_completed(to_do)
    done_iter = tqdm(done_iter, total=10000)
    for index, future in enumerate(done_iter):
        pass



# for i in tqdm(range(1000)):
#     time.sleep(random.randint(1, 11) * 0.01)