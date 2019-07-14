'''
    @ -*- coding: utf-8 -*-
    @ __author__ = "陈宸"
    @ Project: 自己写的代码
    @ FileName: 10快速排序.py
    @ Date: 2019/7/3


'''

def quick_sort(alist, first, last):

    if first >= last:
        return
    mid_value = alist[first]
    low = first
    high = last
    while low < high:
        # high 左移
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]

        # low 右移
        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]

    # 退出循环时：low = high
    alist[low] = mid_value

    # 对low左边列表排序
    quick_sort(alist, first, low-1)
    # 对low右边列表排序
    quick_sort(alist, low+1, last)


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    quick_sort(li, 0, len(li)-1)
    print(li)