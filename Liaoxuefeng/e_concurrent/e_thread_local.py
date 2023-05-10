"""
ThreadLocal
多线程环境下，每一个线程均可以使用所属进程的全局变量。
如果一个线程对全局变量进行了修改，将会影响到其他所有的线程。
为了避免多个线程同时对变量进行修改，引入了线程同步机制，通过互斥锁，条件变量或者读写锁来控制对全局变量的访问。

"""
import threading

# 创建全局ThreadLocal对象:
local_school = threading.local()


# 一个线程执行过程中的一个函数
def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))


# 定义一个线程需要执行的方法
def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()


# 对于Thread-A来说, Alice这个学生类就是这个线程的全局变量
t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
