'''
    @ -*- coding: utf-8 -*-
    @ __author__ = "陈宸"
    @ Project: 自己写的代码
    @ FileName: 双向链表.py
    @ Date: 2019/6/29


'''


class Node:
    '''节点'''
    def __init__(self, item):
        self.element = item
        self.next = None
        self.prev = None


class DoubleLinkList:
    '''双链表'''
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        # 链表是否为空
        return self.__head is None

    def length(self):
        # 链表长度
        cur = self.__head  # 游标，用来移动便利节点
        count = 0
        while cur != None:
            count += 1
            cur = cur.next

    def travel(self):
        # 遍历链表
        cur = self.__head
        while cur != None:
            print(cur.element, end=' ')
            cur = cur.next
        print('')

    def add(self, item):
        #链表头部添加
        node = Node(item)
        node.next = self.__head
        self.__head = node.prev
        node.next.prev = node

    def append(self, item):
        #链表尾部添加
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, pos, item):
        # 指定位置添加
        if pos <= 0:
            self.add(item)
        elif pos >= (self.length()-1):
            self.append(item)
        else:
            cur = self.__head
            node = Node(item)
            count = 0
            while count < pos :
                count += 1
                cur = cur.next
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

    def remove(self, item):
        # 删除节点
        cur = self.__head
        while cur is not None:
            if cur.element == item:
                if cur == self.__head:
                    self.__head = cur.next
                    cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        cur.next.prev = cur.prev
                        break
            else:
                cur = cur.next

    def search(self, item):
        #查找节点是否存在
        n = 0
        cur = self.__head
        while cur != None:
            if cur.element == item:
                return n
            else:
                cur = cur.next
                n += 1
        return False


if __name__ == '__main__':
    l = DoubleLinkList()
    # print(l.is_empty())

    # l.append(1)
    # print(l.is_empty())
    # print(l.length())
    # l.append(1)
    # l.add(3)
    l.append(1)
    l.append(2)
    l.append(3)
    l.append(4)
    l.append(5)
    l.travel()
    l.remove(2)
    l.remove(3)
    print('=========')
    l.travel()