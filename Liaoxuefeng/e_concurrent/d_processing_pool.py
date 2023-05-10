"""
线程池
"""
import os
import random
import time
from multiprocessing import Pool


# 一个需要长时间执行的任务, 实际上使用sleep()函数使进程休眠随机事件
def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)  # 分配一个有4个进程的进程池
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))  # 异步执行5个任务
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
"""
执行结果:
Parent process 14496.
Waiting for all subprocesses done...
Run task 0 (9860)...
Run task 1 (22432)...
Run task 2 (25404)...
Run task 3 (23928)...
Task 0 runs 0.77 seconds.
Run task 4 (9860)...
Task 4 runs 0.67 seconds.
Task 2 runs 1.52 seconds.
Task 3 runs 2.03 seconds.
Task 1 runs 2.39 seconds.
All subprocesses done.
由于创建了4个进程的池子, 所以Task4需要等待其它Task运行结束才能开始.
如果改为Pool(5), 则可以一次全部运行完毕
"""
