'''
    @ -*- coding: utf-8 -*-
    @ __author__ = "陈宸"
    @ Project: 自己写的代码
    @ FileName: 树.py
    @ Date: 2019/7/15


'''

class Node:
    def __init__(self, item):
        self.element = item
        self.lchild = None
        self.rchild = None

class Tree:
    '''二叉树'''
    def __init__(self):
        self.root = None

    def add(self, item):
        '''广度遍历添加元素'''
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]

        while queue:
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)

    def breadth_travel(self):
        '''广度遍历'''
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.element, end=' ')
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    def preorder(self, node):
        '''先序遍历'''
        if node is None:
            return

        print(node.element, end=' ')
        self.preorder(node.lchild)
        self.preorder(node.rchild)

    def inorder(self, node):
        '''中序遍历'''
        if node is None:
            return

        self.inorder(node.lchild)
        print(node.element, end=' ')
        self.inorder(node.rchild)

    def posorder(self, node):
        '''后序遍历'''
        if node is None:
            return

        self.posorder(node.lchild)
        self.posorder(node.rchild)
        print(node.element, end=' ')


if __name__ == '__main__':
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breadth_travel()
    print(' ')
    tree.preorder(tree.root)
    print(' ')
    tree.inorder(tree.root)
    print(' ')
    tree.posorder(tree.root)
