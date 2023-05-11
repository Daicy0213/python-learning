import queue, time, random, threading, requests
from bs4 import BeautifulSoup

urls = [
    f'https://www.cnblogs.com/#p{page}'
    for page in range(1, 50 + 1)
]


def craw(url):
    r = requests.get(url)
    return r.text


def parse(html):
    soup = BeautifulSoup(html, "html.parser")
    # 获得所有<a class="post-item-title">
    links = soup.find_all("a", class_="post-item-title")
    # 返回一个list对象, 其中每个元素都是一个元组, 每个元组的第一个元素为href,第二个元素为标签内容
    return [(link["href"], link.get_text()) for link in links]


if __name__ == '__main__':
    for result in parse(craw(urls[2])):
        print(result)
"""结果
('https://www.cnblogs.com/techcorner/p/17391439.html', '这个字段我明明传了呀，为什么收不到 - Spring 中首字母小写，第二个字母大写造成的参数问题')
.....
('https://www.cnblogs.com/Jcloud/p/17390152.html', 'Webpack5构建性能优化：构建耗时从150s到60s再到10s')
('https://www.cnblogs.com/kenx/p/17390049.html', '金三银四好像消失了，IT行业何时复苏！')
"""


# 生产者 负责将url爬取为html,并将html放入html_queue队列
def do_craw(url_queue: queue.Queue, html_queue: queue.Queue):
    while True:
        url = url_queue.get()
        html = craw(url)
        html_queue.put(html)
        # 打印当前线程的名字
        print(threading.current_thread().name, f"craw{url}", "url_queue.size=", url_queue.qsize())


# 消费者 负责消费html_queue中的数据, 将html解析为parse函数的形式
def do_parse(html_queue: queue.Queue):
    while True:
        html = html_queue.get()
        results = parse(html)
        for result in results:
            # 'a' 表示追加写入
            with open("g_data.txt", 'a') as f:
                f.write(str(result) + "\n")
        print(threading.current_thread().name, f"results.size", len(results),
              "html_queue.size=", html_queue.qsize())


if __name__ == '__main__':
    html_queue = queue.Queue()
    url_queue = queue.Queue()
    for url in urls:
        url_queue.put(url)

    for idx in range(2):
        t = threading.Thread(target=do_craw, args=(url_queue, html_queue), name=f"craw{idx}")
        t.start()

    for idx in range(2):
        t = threading.Thread(target=do_parse, args=(html_queue,), name=f"parse{idx}")
        t.start()
