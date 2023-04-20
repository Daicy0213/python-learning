"""
定义一颗二叉排序(搜索)树
采用"节点与引用"表示法实现二叉搜索树，它类似于我们在实现链表和表达式树时采用的方法。
不过，由于必须创建并处理一棵空的二 叉搜索树，因此我们将使用两个类。
一个称作BinarySearchTree，另一个称作TreeNode。
BinarySearchTree类有一个引用，指向作为二叉搜索树根节点的TreeNode类。
大多数情况下，外面这个类的方法只是 检查树是否为空。
如果树中有节点，请求就被发往BinarySearchTree类的私有方法，这个方法以根节点作为参数。
当树为空，或者想删除根节点的键时，需要采取特殊措施。
"""
import json


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    # 以下写法在树中有多个节点后报错 ValueError: Circular reference detected
    # 原因是因为当树中有多个节点是, 如root -> left, root中有left对象, 而left对象中的parent又包含root对象, 造成循环引用
    # 故需要删除dict的中parent属性即可
    # def __str__(self):
    #     return json.dumps(self.root, default=lambda obj: obj.__dict__)

    def __iter__(self):
        if self:
            return self.root.__iter__()

    def length(self):
        return self.size

    # 插入新的节点, 检查树是否已经有根节点，若没有，就创建一个TreeNode，并将其作为树的根节点；
    # 若有，就调用私有的递归辅助函数_put，并根据以下算法 在树中搜索。
    def put(self, data, weight):
        if self.root:
            self._put(data, weight, self.root)
        else:
            self.root = TreeNode(data, weight)
        self.size = self.size + 1

    def _put(self, data, weight, current_node):
        if data < current_node.data:  # 小于根节点, 插入左子树
            if current_node.left:  # 左子树不为空则递归查找
                self._put(data, weight, current_node.left)
            else:  # 左子树为空则直接插入
                current_node.left = TreeNode(data, weight, parent=current_node)
        else:  # 大于根节点, 插入右子树
            if current_node.right:
                self._put(data, weight, current_node.right)
            else:
                current_node.right = TreeNode(data, weight, parent=current_node)

    def get(self, data):
        if self.root:
            res = self._get(data, self.root)
            if res:
                return res.weight
            else:
                return None
        else:
            return None

    def _get(self, data, current_node):
        if not current_node:  # 如果节点为空
            return None
        elif current_node.data == data:  # 找到对应节点则返回
            return current_node
        elif data < current_node.data:  # 如果小于则在左子树中, 递归查找
            return self._get(data, current_node.left)
        else:  # 如果大于则在右子树中, 递归查找
            return self._get(data, current_node.right)

    # __setitem__和__getitem__ 可以用来重载[]运算符, 相当于可以像操作一个dict一样操作二叉树结构了
    def __setitem__(self, k, v):
        self.put(k, v)

    def __getitem__(self, item):
        return self.get(item)

    # __contains__ 用来重载in关键字(运算符), 可以判断该类中是否存在对应的元素
    def __contains__(self, item):
        if self._get(item, self.root):
            return True
        else:
            return False


"""
树节点类
显式地将父节点记录为一个属性,方便删除操作
左右子树及父节点都不适合使用私有变量, 因为
"""


class TreeNode:
    def __init__(self, data, weight, left=None, right=None, parent=None):
        self._data = data  # 节点中保存的数据
        self._weight = weight  # 权重
        self.left = left  # 左子树节点
        self.right = right  # 右子树节点
        self.parent = parent  # 父节点

    def __str__(self):
        return json.dumps(self, default=lambda obj: obj.__dict__)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        self._weight = weight

    def is_left(self):
        return self.parent and self.parent.get_left() is self

    def is_right(self):
        return self.parent and self.parent.get_right() is self

    def is_root(self):
        return self.parent is not None

    def is_leaf(self):
        return not (self.right or self.left)

    def has_any_child(self):
        return self.right or self.left

    def has_both_child(self):
        return self.right and self.left

    def replace_node_data(self, data, weight, lc, rc):
        self._data = data
        self._weight = weight
        self.left = lc
        self.right = rc
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self


tree = BinarySearchTree()
node1 = TreeNode(1, 2)
node2 = TreeNode(2, 2)
node3 = TreeNode(3, 2)
tree[5] = 2
tree[3] = 2
print(tree[3])
print(3 in tree)
