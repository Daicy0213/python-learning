"""通过定义一个继承threading.Thread的类来设置线程
需要实现定时结束该线程的方法
"""
import threading
import time


class MyThread(threading.Thread):
    def run(self):
        print('Thread is running...')
        # 让线程暂停 5 秒
        time.sleep(5)
        print('Thread is paused...')


# 创建线程对象并启动线程
t = MyThread()
t.start()
