"""用于解决线程安全问题的锁的用法
用法一: try-finally模式
用法二: with模式
"""
import threading

lock = threading.Lock()


class Account:
    """定义一个账户类
    用于模拟多线程状态下, 用户取钱的过程
    """

    def __init__(self, balance):
        self.balance = balance


def draw(account: Account, amount):
    """取钱的函数
    account表示账户类
    amount表示需要取得钱的数量"""
    with lock:  # 当使用lock时, 则不会出现错误
        if account.balance >= amount:
            print(threading.current_thread().name, "操作成功")
            account.balance -= amount
            print(threading.current_thread().name, "账户余额为:", account.balance)
        else:
            print(threading.current_thread().name, "操作失败, 账户余额不足")


if __name__ == '__main__':
    account = Account(800)
    thread1 = threading.Thread(target=draw, args=(account, 600), name='T1')
    thread2 = threading.Thread(target=draw, args=(account, 600), name='T2')
    thread2.start()
    thread1.start()
