"""asyncio异步io
asyncio的编程模型就是一个消息循环。我们从asyncio模块中直接获取一个 EventLoop 的引用，
然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO。

EventLoop可以看成一个大脑, 它在面对了多个可以执行的任务的时候, 决定了接下来要执行哪个任务.
asyncio与线程不同, 不存在系统级的切换, 但它需要每一个任务主动告诉 EventLoop 自己的结束时间,
以方便 EventLoop 选择新的任务继续执行.

因此, asyncio不存在竞争冒险而产生死锁的问题.
"""
import asyncio
import threading

print("-" * 15, "coroutine-1Job", "-" * 15)
"""
@asyncio.coroutine把一个generator标记为coroutine类型，然后，我们就把这个coroutine扔到EventLoop中执行。

hello()会首先打印出Hello world!，然后，yield from语法可以让我们方便地调用另一个generator。
由于asyncio.sleep()也是一个coroutine，所以线程不会等待asyncio.sleep()，
而是直接中断并执行下一个消息循环。
当asyncio.sleep()返回时，线程就可以从yield from拿到返回值（此处是None），然后接着执行下一行语句。

把asyncio.sleep(1)看成是一个耗时1秒的IO操作，在此期间，主线程并未等待，而是去执行EventLoop中其他可以执行的coroutine了，
因此可以实现并发执行。
"""


async def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1)模拟io操作:
    r = await asyncio.sleep(1)
    print("Hello again!")


# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
"""loop.close()
这里注释掉了关闭操作, 因为单一线程只能创建一个Eventloop, 如果关闭了以后在后面的代码再重新创建则会报错:
RuntimeError: Event loop is closed
sys:1: RuntimeWarning: coroutine 'hello' was never awaited
"""
# loop.close()

"""用Task封装两个coroutine"""
print("-" * 15, "coroutine-2Jobs", "-" * 15)


async def hello():
    print('Hello world! (%s)' % threading.current_thread().name)
    r = await asyncio.sleep(1)
    print('Hello again! (%s)' % threading.current_thread().name)


# 获取EventLoop:
# loop = asyncio.get_event_loop()
tasks = [loop.create_task(hello()) for i in range(2)]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
