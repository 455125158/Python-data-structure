'''
    @ -*- coding: utf-8 -*-
    @ __author__ = "陈宸"
    @ Project: 自己写的代码
    @ FileName: 8插入排序.py
    @ Date: 2019/7/2


'''


def insert_sort(alist):
    # 从无序列表中取出多少个元素执行循环
    for j in range(1, len(alist)):
        i = j   # 内层循环的起始值
        # 从无序列表中取出元素（i的位置），插入有序列表中
        while i > 0:
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
                i -= 1
            else:
                break

if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    insert_sort(li)
    print(li)