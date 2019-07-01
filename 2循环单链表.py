'''
    @ -*- coding: utf-8 -*-
    @ __author__ = "陈宸"
    @ Project: 自己写的代码
    @ FileName: 循环单链表.py
    @ Date: 2019/6/25


'''

class Node:
    '''节点'''
    def __init__(self, element):
        self.element = element
        self.next = None


class SingleCycleList:
    '''单向循环列表'''
    def __init__(self, node=None):
        self.__head = node
        if node:
            node.next = node

    def is_empty(self):
        #链表是否为空
        return self.__head == None

    def length(self):
        #链表长度
        if self.is_empty():
            return 0
        cur = self.__head
        count = 1
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        #遍历整个链表
        cur = self.__head
        if self.is_empty():
            return 0
        else:
            while cur.next != self.__head:
                print(cur.element, end=' ')
                cur = cur.next
            # 退出循环，cur指向尾节点
            print(cur.element)

    def add(self, item):
        #链表头部添加元素
        node =  Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            # 退出循环，cur指向尾节点
            node.next = self.__head
            self.__head = node
            cur.next = self.__head

    def append(self, item):
        #链表尾部添加元素
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            cur.next = node

    def insert(self,pos, item):
        #指定位置添加元素
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
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

    def remove(self, item):
        #删除节点
        if self.is_empty():
            return

        cur = self.__head
        pre = None
        while cur.next != self.__head:
            if cur.element == item:
                # 头结点
                if cur == self.__head:
                    # 找尾节点
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                # 中间情况
                else:
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        # 退出循环，cur指向尾节点
        if cur.element == item:
            if cur == self.__head:
                # 连表只有一个节点
                self.__head = None
            else:
                pre.next = cur.next


    def search(self, item):
        #查找节点是否存在
        if self.is_empty():
            return False
        cur = self.next
        while cur.next != self.__head:
            if cur.element == item:
                return True
            else:
                cur = cur.next
        if cur.element == item:
            return True
        return False

if __name__ == '__main__':
    l = SingleCycleList()
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
    l.remove(1)
    l.remove(5)
    print('=========')
    l.travel()
