"""hashlib
python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。

什么是摘要算法呢？摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。

举个例子，你写了一篇文章，内容是一个字符串'how to use python hashlib - by Michael'，并附上这篇文章的摘要是'2d73d4f15c0db7f5ecb321b6a65e5d6d'。如果有人篡改了你的文章，
并发表为'how to use python hashlib - by Bob'，你可以一下子指出Bob篡改了你的文章，因为根据
'how to use python hashlib - by Bob'计算出的摘要不同于原始文章的摘要。

可见，摘要算法就是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest，目的是为了发现原始数据是否被人篡改过。

摘要算法之所以能指出数据是否被篡改过，就是因为摘要函数是一个单向函数，计算f(data)很容易，但通过digest反推data却非常困难。
而且，对原始数据做一个bit的修改，都会导致计算出的摘要完全不同。
所以最常见的用处是针对用户的密码进行加密, 即使是运维人员可以看到digest, 却无法反推密码的data
"""
import hashlib
import random

"""MD5算法
MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit/16字节，通常用一个32位的16进制字符串表示。
"""
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

# 如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的：
md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

"""SHA1算法
SHA1的结果是160 bit/20字节，通常用一个40位的16进制字符串表示。
比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法不仅越慢，而且摘要长度更长。
"""
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

"""加盐
由于常用口令的MD5值很容易被计算出来，所以，要确保存储的用户口令不是那些已经被计算出来的常用口令的MD5，
这一方法通过对原始口令加一个复杂字符串来实现，俗称“加盐”：

def calc_md5(password):
    return get_md5(password + 'the-Salt')
经过Salt处理的MD5口令，只要Salt不被黑客知道，即使用户输入简单口令，也很难通过MD5反推明文口令。

但是如果有两个用户都使用了相同的简单口令比如123456，在数据库中，将存储两条相同的MD5值，这说明这两个用户的口令是一样的。
有没有办法让使用相同口令的用户存储不同的MD5呢？

如果假定用户无法修改登录名，就可以通过把登录名作为Salt的一部分来计算MD5，从而实现相同口令的用户也存储不同的MD5。
根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5：
"""
print("-" * 15, "模拟用户注册和登录的操作", "-" * 15)
# 模拟数据库
db = {}


# 通过md5计算字符串的摘要
def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()


# 用户类
class User(object):
    def __init__(self, username, password):
        self.username = username
        # 随机生成的盐
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + self.salt)


# 注册
def register(username: str, password):
    user = User(username, password)
    db[username] = user


# 注册用户
register('michael', '123456')
register('bob', 'abc999')
register('alice', 'alice2008')
for username, user in db.items():
    print(f"username: {username}, password: {user.password}, salt: {user.salt}")


def login(username, password):
    user = db[username]
    return user.password == get_md5(password + user.salt)


assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
