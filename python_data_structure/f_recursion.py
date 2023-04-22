"""递归"""
from turtle import *


# 使用递归将整数转换成以2~16为进制基数的字符串
def to_str(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return to_str(n // base, base) + convertString[n % base]


# 将128转换为16进制
print('Use recursion to convert 128 to hexadecimal:', to_str(128, 16))
print('---------------------')

# 设置绘制的对象
draw = 'tree'

myTurtle = Turtle()
myWin = myTurtle.getscreen()


# 绘制一个螺旋
def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle, lineLen - 5)


# 绘制一个分形树
def tree(branch_len, t):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        tree(branch_len - 15, t)
        t.left(40)
        tree(branch_len - 10, t)
        t.right(20)
        t.backward(branch_len)


if draw == 'spiral':
    drawSpiral(myTurtle, 100)
    myWin.exitonclick()
else:
    myTurtle.left(90)
    myTurtle.up()
    myTurtle.backward(300)
    myTurtle.down()
    myTurtle.color('green')
    tree(110, myTurtle)
    myWin.exitonclick()
