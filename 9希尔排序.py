'''
    @ -*- coding: utf-8 -*-
    @ __author__ = "陈宸"
    @ Project: 自己写的代码
    @ FileName: 9希尔排序.py
    @ Date: 2019/7/2


'''
def shell_sort(alist):
    n = len(alist)
    gap = n // 2
    while gap >= 1:         # 与普通插入算法的区别就是gap步长
        for j in range(gap, n):   # J从gap开始取，gap之前的都是用来与J比较的
            i = j
            while i > 0:
                if alist[i] > alist[i-gap]:
                    alist[i], alist[i-gap] = alist[i-gap], alist[i]
                    i -= gap
                else:
                    break
        gap //= 2

if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    shell_sort(li)
    print(li)