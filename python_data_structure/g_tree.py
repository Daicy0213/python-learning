"""
树
"""
from d_stack import Stack


# 定义一颗二叉树
class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # 插入左节点
    def insert_left(self, new):
        # 如果该子树左子树为空则直接插入
        if self.left is None:
            self.left = BinaryTree(new)
        # 如果该子树左子树不为空, 则将新插入的节点设为左子树, 并将原左子树向下移动到新左子树的左节点
        else:
            t = BinaryTree(new)
            t.left = self.left
            self.left = t

    # 插入右节点
    def insert_right(self, new):
        if self.right is None:
            self.right = BinaryTree(new)
        else:
            t = BinaryTree(new)
            t.right = self.right
            self.right = t

    # 获取左子树
    def get_left(self):
        return self.left

    # 获取右子树
    def get_right(self):
        return self.right

    # 设置节点值
    def set_data(self, obj):
        self.data = obj

    # 获取节点值
    def get_data(self):
        return self.data


def op_parser(exp):
    result = []
    for c in exp:
        if c != ' ':
            result.append(c)
    return result


# 使用树和栈来解析表达式 用于解析((7 + 3) * (5 - 2))这样的表达式
def build_parse_tree(exp):
    exp_list = op_parser(exp)
    stack = Stack()
    tree = BinaryTree('')
    stack.push(tree)
    current_tree = tree
    for i in exp_list:
        if i == '(':
            current_tree.insert_left('')
            stack.push(current_tree)
            current_tree = current_tree.get_left()
        elif i not in '+-*/)':
            current_tree.set_data(eval(i))  # eval()函数: 在全局变量和局部变量的上下文中评估给定的源
            parent = stack.pop()
            current_tree = parent
        elif i in '+-*/':
            current_tree.set_data(i)
            current_tree.insert_right('')
            stack.push(current_tree)
        elif i == ')':
            current_tree = stack.pop()
        else:
            raise ValueError('Unknown Operator: ' + i)
    return tree
