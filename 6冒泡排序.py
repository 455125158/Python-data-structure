'''
    @ -*- coding: utf-8 -*-
    @ __author__ = "陈宸"
    @ Project: 自己写的代码
    @ FileName: 冒泡排序.py
    @ Date: 2019/7/1


'''

def bubble_sort(alist):
    # 冒泡排序
    for j in range(0, len(alist)-1):
        # 一共循环次数
        count = 0
        for i in range(0, len(alist)-1-j):
            # 指针走的步数
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                count += 1
        if 0 == count:
            return alist

if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    bubble_sort(li)
    print(li)

