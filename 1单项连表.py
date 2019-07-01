'''
@ -*- coding: utf-8 -*-
@ __author__ = "陈宸"
@ Project: 自己写的代码
@ FileName: 单项连表.py
@ Date: 2019/6/21


'''


class Node:
    '''节点'''
    def __init__(self, element):
        self.element = element
        self.next = None

class SingleLinkList:
    '''单链表'''
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        # 链表是否为空
        return self.__head == None

    def length(self):
        # 链表长度
        cur = self.__head              # 游标，用来移动便利节点
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        # 遍历整个链表
        cur = self.__head
        while cur != None:
            print(cur.element, end=' ')
            cur = cur.next

    def add(self,item):
        # 链表头部添加元素
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self,item):
        # 链表尾部添加元素
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        # 指定位置添加元素
        if pos <= 0:
            self.add(item)
        elif pos >= (self.length()-1):
            self.append(item)
        else:
            pre = self.__head
            count = 0
            while count < pos-1:
                count += 1
                pre = pre.next
            # 循环结束后，pre指向pos-1
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self,item):
        # 删除节点
        cur = self.__head
        pre = None
        while cur != None:
            if cur.element == item:
                if cur == self.__head:    # 删头结点
                    self.__head = cur.next
                else:
                    # pre.next = pre.next.next
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self,item):
        # 查找节点是否存在
        n = 0
        cur = self.__head
        while cur != None:
            if cur.element == item:
                return n
            else :
                cur = cur.next
                n += 1
        return False

if __name__ == '__main__':
    l = SingleLinkList()
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



