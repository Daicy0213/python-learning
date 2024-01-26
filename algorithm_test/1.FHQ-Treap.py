# 请在此输入您的代码
n, m = map(int, input().split())
s = [ x for x in range(n+1)]

for i in range(m):
    l, r = map(int, input().split())
    x = r - l
    temp = s[r: l - 1: -1]
    s[l: r + 1] = temp

for i in range(1, n + 1):
    if i != n:
        print(s[i], end='')
        print(" ", end='')
    else:
        print(s[i], end='')
