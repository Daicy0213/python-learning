import os
from multiprocessing import Process

platform = os.name

if platform == 'posix':  # Only works on Unix/Linux/Mac:
    print('Process (%s) start...' % os.getpid())
    """
    fork()函数调用一次, 返回两次:
    操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。
    子进程永远返回0，而父进程返回子进程的ID。
    因为，一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID。
    """
    pid = os.fork()
    if pid == 0:
        # getppid() = get parent pid 获取其父进程的pid
        print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
    else:
        print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
else:
    # 子进程要执行的代码
    def run_proc(name):
        print('Run child process %s (%s)...' % (name, os.getpid()))


    if __name__ == '__main__':
        print('Parent process %s.' % os.getpid())
        p = Process(target=run_proc, args=('test',))
        print('Child process will start.')
        p.start()
        p.join()
        print('Child process end.')
