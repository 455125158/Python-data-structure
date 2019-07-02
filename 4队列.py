'''
    @ -*- coding: utf-8 -*-
    @ __author__ = "陈宸"
    @ Project: 自己写的代码
    @ FileName: 队列.py
    @ Date: 2019/7/1


'''

class Queue:
    def __init__(self):
        self.__list = []

    def enqueue(self, item):
    # 往队列中添加一个item元素
        self.__list.append(item)

    def dequeue(self):
    # 从队列头部删除一个元素
        return self.__list.pop(0)

    def is_empty(self):
    # 判断一个队列是否为空
        return self.__list is not None

    def size(self):
    # 返回队列的大小
        return len(self.__list)


class Deque:
    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        # 往队列中添加一个item元素
        self.__list.append(item)

    def dequeue(self):
        # 从队列头部删除一个元素
        return self.__list.pop(0)

    def is_empty(self):
        # 判断一个队列是否为空
        return self.__list is not None

    def size(self):
        # 返回队列的大小
        return len(self.__list)