"""hmac
HMAC（Hash-based Message Authentication Code，基于哈希函数的消息鉴别码）是一种利用哈希算法和密钥对消息进行认证的技术。

hmac 库是 Python 内置的标准库之一，用于实现 HMAC 算法。

在加密通信中，HMAC 通常用于保护消息的完整性和真实性。
具体来说，可以使用 HMAC 生成一个与消息关联的认证标记（MAC），通过将该标记发送到接收方并与接收方计算自己的标记进行比较，
以确保消息来自于预期的发送方且没有被篡改过。

例如，在 Web 应用程序中，可以使用 HMAC 来保护用户登录会话 Cookie，以防止攻击者使用伪造的 Cookie 访问用户账户。
具体实现时，可以在服务器端的代码中使用 hmac 库计算客户端发送的 Cookie 的 HMAC 值，并将其与服务器上保存的该用户的 HMAC 值进行比较。
如果两个值不匹配，则表明该 Cookie 可能已被篡改或伪造。

在 Python 中，可以使用 hmac 库提供的函数轻松实现 HMAC 算法及其应用场景，其中最常用的函数包括 hmac.new()、hmac.compare_digest() 等。

需要注意的是，在使用 HMAC 时需要选择合适的哈希函数、密钥长度等参数，并严格遵循安全最佳实践以确保算法的安全性。
"""
import hmac

message = b'Hello, world!'
key = b'secret'
h = hmac.new(key, message, digestmod='MD5')
# 如果消息很长，可以多次调用h.update(msg)
print(h.hexdigest())
