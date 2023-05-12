"""线程池ThreadPoolExecutor的使用
用法一:
with ThreadPoolExecutor() as pool:
    results = pool.map(fn, args)

    for result in results:
        print(result)

用法二:
with ThreadPoolExecutor() as pool:
    futures = [pool.submit(fn, arg)
                for arg in args]

    # 顺序执行, 按照参数顺序顺序依次返回, 但是如果某一个线程阻塞, 则可能导致所有线程都等待该线程
    for future in futures:
        print(future.result())

    # 先结束的先返回
    for future in as_completed(futures):
        print(future.result())
"""
from concurrent.futures import ThreadPoolExecutor, as_completed


def fn(a):
    return a + a


with ThreadPoolExecutor() as pool:
    results = pool.map(fn, [1, 2, 3])
    print("=" * 5, "方式一", "=" * 5)
    for result in results:
        print(result)

with ThreadPoolExecutor() as pool:
    futures = [pool.submit(fn, arg)
               for arg in [1, 2, 3]]
    print("=" * 5, "方式二, 非顺序", "=" * 5)
    # as_completed 并非按照顺序返回
    for future in as_completed(futures):
        print(future.result())

    print("=" * 5, "方式二, 顺序", "=" * 5)
    for future in futures:
        print(future.result())
