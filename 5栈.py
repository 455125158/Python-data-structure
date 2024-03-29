'''
    @ -*- coding: utf-8 -*-
    @ __author__ = "陈宸"
    @ Project: 自己写的代码
    @ FileName: 栈.py
    @ Date: 2019/7/1


'''

class Stack:
    '''栈'''
    def __init__(self):
        self.__list = []

    def push(self, item):
        # 添加一个新的元素item到栈顶
        self.__list.append(item)
    def pop(self):
        # 弹出栈顶元素
        return self.__list.pop()

    def peek(self):
    # 返回栈顶元素
        if self.__list:
            return self.__list[-1]
        else:
            return  None

    def is_empty(self):
    # 判断栈是否为空
        return self.__list is None
    def size(self):
    # 返回栈的元素个数
        return len(self.__list)


