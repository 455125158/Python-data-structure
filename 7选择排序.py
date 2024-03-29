'''
    @ -*- coding: utf-8 -*-
    @ __author__ = "陈宸"
    @ Project: 自己写的代码
    @ FileName: 7选择排序.py
    @ Date: 2019/7/1


'''

def select_sort(alist):
    n = len(alist)  # 长度不算0
    for j in range(n-1):
        min_index = j
        for i in range(j+1, n):
            if alist[min_index] > alist[i]:
                min_index = i
        alist[j], alist[min_index] = alist[min_index], alist[j]

if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    select_sort(li)
    print(li)