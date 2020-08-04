from typing import List

from data_strutcure.ListNode import ListNode


class LinkedList:
    def __init__(self, l: List):
        next = None
        for val in l[::-1]:
            next = ListNode(val, next)
        self.node = next

    def __repr__(self):
        node_list = []
        cur = self.node
        while cur:
            node_list.append(cur.val)
            cur = cur.next
        return 'LinkedList[' + ', '.join([str(val) for val in node_list]) + ']'
