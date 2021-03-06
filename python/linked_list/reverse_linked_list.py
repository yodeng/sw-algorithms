#!/usr/bin/env python

# encoding: utf-8


"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: reverse_linked_list.py

@time: 2018/1/16 15:58

@desc: 反转链表

@hint: 多种解法， 递归较为常用
"""

from singly_linked_list_implementation import LinkedList

def create_list():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    return ll

#非递归
def reverse_linked_list_one(root_node):
    if root_node is None:
        return root_node
    prev = None
    while root_node:
        cur = root_node
        root_node = root_node.next
        cur.next = prev
        prev = cur
    return prev


#递归: 在反转当前节点之前先反转后续节点
def reverse_linked_list_two(root_node):
    if root_node is None or root_node.next is None:
        return root_node
    temp_node = reverse_linked_list_two(root_node.next)

    #先反转后续节点，在当前层考虑， 注意递归终止，不要陷入递归误区(陷入递归)
    root_node.next.next = root_node
    root_node.next = None
    return temp_node


if __name__ == '__main__':
    ll = create_list()
    ll.print_list_two()
    ll.head = reverse_linked_list_one(ll.head)
    ll.print_list_two()
