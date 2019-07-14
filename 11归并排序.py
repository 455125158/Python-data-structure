'''
    @ -*- coding: utf-8 -*-
    @ __author__ = "陈宸"
    @ Project: 自己写的代码
    @ FileName: 11归并排序.py
    @ Date: 2019/7/4


'''

def merge_sort(alist):
    n = len(alist)
    if n <= 1:
        return alist
    mid = n//2

    # 得到2个有序的序列
    left_li = merge_sort(alist[:mid])
    right_li = merge_sort(alist[mid:])

    # 把2个有序的序列合并
    left_pointer, right_pointer = 0, 0
    result = []

    while left_pointer < len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] < right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1

    result += left_li[left_pointer:]
    result += right_li[right_pointer:]
    return result


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    a = merge_sort(li)
    print(li)
    print(a)
