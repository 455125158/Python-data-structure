'''
    @ -*- coding: utf-8 -*-
    @ __author__ = "陈宸"
    @ Project: 自己写的代码
    @ FileName: 12二分查找.py
    @ Date: 2019/7/4


'''


def binary_search(alist, item):
    # 递归
    n = len(alist)
    if n > 0:
        mid = n//2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return binary_search(alist[:mid], item)
        else:
            return binary_search(alist[mid+1:], item)
    return False


def binary_search_2(alist, item):
    # 非递归
    n = len(alist)
    first = 0
    last = n-1
    while first <= last:
        mid = (first + last)//2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            last = mid - 1
        else:
            first = mid +1
    return False






if __name__ == '__main__':
    li = [17, 20, 26, 31, 44, 54, 77, 93, 105]
    print(binary_search(li, 93))
    print(binary_search(li, 123))
