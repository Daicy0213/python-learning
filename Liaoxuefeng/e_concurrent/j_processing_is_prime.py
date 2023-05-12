"""使用多进程计算一个数字是否为素数
可以看到ThreadPool和ProcessPool的用法基本一致
"""
import math
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

PRIMES = [112272535095293] * 50


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    """
    math.sqrt(x): 求x的平方根
    math.floor(x): 返回一个整数 int，表示向下舍入的数字。
    例如:
    math.floor(0.6): 0
    math.floor(1.4): 1
    """
    sqrt_n = int(math.floor(math.sqrt(n)))
    # range(start, stop[, step]) : 从3开始, 每次增加2, 到sqrt_n+1为止
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def single_thread():
    start = time.time()
    for num in PRIMES:
        is_prime(num)
    print(f"单线程执行完毕, 用时:{time.time() - start}s")


def multi_thread():
    start = time.time()
    with ThreadPoolExecutor() as pool:
        pool.map(is_prime, PRIMES)
    print(f"多线程执行完毕, 用时:{time.time() - start}s")


def multi_process():
    start = time.time()
    with ProcessPoolExecutor() as pool:
        pool.map(is_prime, PRIMES)
    print(f"多进程程执行完毕, 用时:{time.time() - start}s")


if __name__ == '__main__':
    single_thread()
    multi_thread()
    multi_process()
