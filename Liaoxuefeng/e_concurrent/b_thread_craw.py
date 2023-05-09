"""
使用单线程和多线程爬取网页
"""

import requests
import threading
import time

# 访问以下50个网页
urls = [
    f'https://www.cnblogs.com/#p{page}'
    for page in range(1, 50 + 1)
]

# 结果: ['https://www.cnblogs.com/#p1', 'https://www.cnblogs.com/#p2',....]
print(urls)


def craw(url):
    r = requests.get(url)
    print(url, len(r.text))


# 使用单线程爬取50个网页
def single_thread():
    start_time = time.time()
    for url in urls:
        craw(url)
    print(f'单线程爬取的时间为{time.time() - start_time}s')


# 使用多线程爬取
def multi_thread():
    start_time = time.time()
    threads = []
    for url in urls:
        threads.append(
            threading.Thread(target=craw, args=(url,))
        )

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()  # 等待线程终结

    print(f'多线程爬取的时间为{time.time() - start_time}s')


single_thread()
# 结果:
# https://www.cnblogs.com/#p1 69682 .....
# https://www.cnblogs.com/#p50 69682
# 单线程爬取的时间为11.415833711624146s

multi_thread()
# 结果:
# https://www.cnblogs.com/#p1 69682
# https://www.cnblogs.com/#p50 69682
# 多线程爬取的时间为0.3929774761199951s
