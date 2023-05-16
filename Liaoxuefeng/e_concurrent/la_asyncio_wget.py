"""
使用asyncio进行wget操作
"""
import asyncio


async def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = await connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    await writer.drain()
    while True:
        line = await reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()


loop = asyncio.get_event_loop()
tasks = [loop.create_task(wget(host)) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

# 结果:
# wget www.sina.com.cn...
# wget www.sohu.com...
# wget www.163.com...
# www.sina.com.cn header > HTTP/1.1 302 Moved Temporarily
# www.sina.com.cn header > Server: nginx
# www.sina.com.cn header > Date: Tue, 16 May 2023 05:44:54 GMT
# www.sina.com.cn header > Content-Type: text/html
# www.sina.com.cn header > Content-Length: 138
# www.sina.com.cn header > Connection: close
# www.sina.com.cn header > Location: https://www.sina.com.cn/
# www.sina.com.cn header > X-Via-CDN: f=sinaedge,s=cmcc.zhengzhou.union.141.nb.sinaedge.com,c=2001:250:4803:1066:6007:e91c:e5e0:99bc;
# www.sohu.com header > HTTP/1.1 302 Found
# www.sohu.com header > Location: https://www.sohu.com/
# www.sohu.com header > Content-Length: 0
# www.sohu.com header > X-NWS-LOG-UUID: 7407332957393750625
# www.sohu.com header > Connection: close
# www.sohu.com header > Server: D0
# www.sohu.com header > Date: Tue, 16 May 2023 05:44:54 GMT
# www.sohu.com header > X-Cache-Lookup: Return Directly
# www.163.com header > HTTP/1.1 301 Moved Permanently
# www.163.com header > Date: Tue, 16 May 2023 05:44:54 GMT
# www.163.com header > Content-Length: 0
# www.163.com header > Connection: close
# www.163.com header > Server: web cache
# www.163.com header > Location: https://www.163.com/
# www.163.com header > Cache-Control: no-cache,no-store,private
# www.163.com header > cdn-user-ip: 2001:250:4803:1066:6007:e91c:e5e0:99bc
# www.163.com header > cdn-ip: 2409:8c44:2:ff0a::f9
# www.163.com header > X-Cache-Remote: MISS
# www.163.com header > cdn-source: baishan
#
# Process finished with exit code 0