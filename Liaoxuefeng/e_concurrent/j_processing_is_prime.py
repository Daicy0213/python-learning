"""使用多进程计算一个数字是否为素数
可以看到ThreadPool和ProcessPool的用法基本一致
"""
import math
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

PRIMES = [112272535095293] * 50
PRIMES_SINGLE = [10000769] * 1


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


def is_prime_complex(n):
    """以下算法使用Clang可以快速得出结果
    但是使用python则需要长时间的计算
    主要用来对比python和Clang的计算速度差距
    """
    k = n
    i = 3
    factor_l = []
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    while k > 1:
        if k % i == 0:
            k /= i
            factor_l.append(i)
        else:
            i += 2
    if len(factor_l) > 1:
        return False
    else:
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


def multi_process_complex():
    start = time.time()
    with ProcessPoolExecutor() as pool:
        pool.map(is_prime_complex, PRIMES_SINGLE)
    print(f"多进程程执行完毕, 用时:{time.time() - start}s")


if __name__ == '__main__':
    single_thread()
    multi_thread()
    multi_process()
    # prime = PRIMES_SINGLE.pop(0)
    # print(is_prime_complex(prime))
    # multi_process_complex()
