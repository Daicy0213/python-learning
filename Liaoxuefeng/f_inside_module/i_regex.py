"""正则表达式"""
import re

r = r'^\d{3}\-\d{3,8}$'
print(re.match(r, '010-12345'))
print(re.match(r, '010 12345'))
# 结果:
# <re.Match object; span=(0, 9), match='010-12345'>
# None


"""可以使用re来切割字符串"""
split = re.split(r'[\s,;]+', 'a,b;; c  d')
print(split)

"""使用re来进行分组"""
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(0))
print(m.group(1))
print(m.group(2))

reg_email = r'^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$'


def is_valid_email(addr):
    if re.match(reg_email, addr):
        return True
    else:
        return False


print(is_valid_email('someone@gmail.com'))
print(is_valid_email('someone@gmail@com'))
