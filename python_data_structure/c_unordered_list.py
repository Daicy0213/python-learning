"""
Node类
首先，节点必须包含列表元素，我们称之为节点的数据变量。其次，节点必须保存指向下一个节点的引用。
在构建节点时，需要为其提供初始值。
"""


class Node(object):
    def __init__(self, init_data):
        self._data = init_data
        self._next = None

    def __str__(self):
        return str(self._data)

    def get_data(self):
        return self._data

    def get_next(self):
        return self._next

    def set_data(self, new_data):
        self._data = new_data

    def set_next(self, new_next):
        self._next = new_next


"""
无序列表（unordered list）是基于节点集合来构建的，每一个节点都通过显式的引用指向下一个节点。
只要知道第一个节点的位置（第一个节点包含第一个元素），其后的每一个元素都能通过下一个引用找到。
非常重要的一点是，列表类本身并不包含任何节点对象，而只有指向整个链表结构中第一个节点的引用。
mylist -> head -> 92 -> 23 -> 95 -> None 
"""


class UnorderedList:
    def __init__(self):
        self._head = None

    def __str__(self):
        current = self._head
        result = 'List: '
        while current is not None:
            result += str(current.get_data())
            result += ", "
            current = current.get_next()

        return result[:-2]

    def is_empty(self):
        return self._head is None

    # 头插法
    def add(self, item):
        temp = Node(item)  # 创建一个Node对象
        temp.set_next(self._head)
        self._head = temp

    def __len__(self):
        current = self._head
        count = 0
        while current is not None:
            count = count + 1
            current = current.get_next()
        return count

    # 查找索引
    def search_index(self, item):
        current = self._head
        index = 0
        while current is not None:
            if current.get_data() is item:
                return index
            else:
                current = current.get_next()
                index += 1

    # 删除, 需要修改next的值
    def remove(self, item):
        current = self._head
        previous = None
        while current is not None:
            if current.get_data() is item:
                if previous is None:
                    self._head = current.get_next()
                    return True
                else:
                    previous.set_next(current.get_next())
                    return True
            else:
                previous = current
                current = current.get_next()


mylist = UnorderedList()
mylist.add(92)
mylist.add(23)
mylist.add(95)
mylist.add(31)
mylist.add(32)

print("length:", len(mylist))
print("is empty:", mylist.is_empty())
print("print:", mylist)
print("index of 23:", mylist.search_index(23))
print("search index of 23:", mylist.search_index(23))
mylist.remove(31)
mylist.remove(32)
print("print after remove:", mylist)

"""
有序链表
"""
print('----------OrderedList-----------')


class OrderedList(UnorderedList):
    # 重写查询
    def search_index(self, item):
        index = 0
        current = self._head
        while current is not None and current.get_data() <= item:
            if current.get_data() is item:
                return index
            else:
                index += 1
                current = current.get_next()
        return -1

    # 重写插入方法
    def add(self, item):

        current = self._head
        previous = None
        stop = False
        while current is not None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()

        node = Node(item)
        if previous is None:
            node.set_next(self._head)
            self._head = node
        else:
            node.set_next(current)
            previous.set_next(node)


mylist2 = OrderedList()
mylist2.add(33)
mylist2.add(30)
mylist2.add(31)
mylist2.add(32)
print(mylist2.search_index(30))
print(mylist2.search_index(32))
print(mylist2.search_index(34))
print(mylist2)
