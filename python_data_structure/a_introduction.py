"""
要展示不同数量级的算法，一个好例子就是经典的异序词检测问题。
如果一个字符串只是重排了另一个字符串的字符，那么这个字符串就是另 一个的异序词，比如heart与earth，以及python与typhon。
为了简化问 题，假设要检查的两个字符串长度相同，并且都是由26个英文字母的小写形式组成的。
我们的目标是编写一个布尔函数，它接受两个字符串， 并能判断它们是否为异序词。
"""

t1 = ('earth', 'heart')
t2 = ('sss1abc', 'cba1ssa')


# 常规方法 时间复杂度为O(n^2)
def anagram_solution1(s1, s2):
    alist = list(s2)  # s2的临时变量

    pos1 = 0  # s1的下标
    flag = True  # 判断是否为异序词的标记

    # 外层遍历, 遍历s1的每一个字母
    while pos1 < len(s1) and flag:
        pos2 = 0  # s2的下标
        found = False  # 是否找到

        # 内层遍历, 遍历s2的每一个字母
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:  # 如果s1的字母等于s2的字母, 则将
                found = True
            else:
                pos2 = pos2 + 1

        if found:  # 如果找到则将s2的临时变量的对应字母设置为空, 避免重复使用
            alist[pos2] = None
        else:
            flag = False

        pos1 += 1
    return flag


print(anagram_solution1(t1[0], t1[1]))
print(anagram_solution1(t2[0], t2[1]))

"""
另一个方案基于这样一个事实：两个异序词有同样数目的a、同 样数目的b、同样数目的c，等等。
要判断两个字符串是否为异序 词，先数一下每个字符出现的次数。因为字符可能有26种，所以使用26个计数器，对应每个字符。
每遇到一个字符，就将对应的计数 器加1。最后，如果两个计数器列表相同，那么两个字符串肯定是异序词。
尽管这个方案的执行 时间是线性的，它还是要用额外的空间来存储计数器。也就是说， 这个算法用空间换来了时间。
这种情形很常见。很多时候，都需要在时间和空间之间进行权衡。本例中，额外使用的空间并不大。
"""


def anagram_solution2(s1, s2):
    counter1 = [0] * 26
    counter2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        counter1[pos] = counter1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        counter2[pos] = counter2[pos] + 1

    j = 0
    flag = True
    while j < 26 and flag:
        if counter1[j] == counter2[j]:
            j = j + 1
        else:
            flag = False

    return flag


print(anagram_solution1(t1[0], t1[1]))
print(anagram_solution1(t2[0], t2[1]))
