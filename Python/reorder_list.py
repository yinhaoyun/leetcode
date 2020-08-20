from Python.data_structure.linked_list import LinkedList
from Python.data_structure.list_node import ListNode


# https://leetcode.com/problems/reorder-list/
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return None
        l = []
        cur = head
        while cur:
            l.append(cur)
            cur = cur.next
        i, j = 0, len(l) - 1
        while i < j:
            temp = l[i].next
            l[i].next = l[j]
            l[j].next = temp
            i, j = i + 1, j - 1
        l[i].next = None
        return head


if __name__ == '__main__':
    s = Solution()
    print(s.reorderList(LinkedList([]).node))  # None
    print(s.reorderList(LinkedList([1]).node))  # 1
    print(s.reorderList(LinkedList([1, 2, 3, 4]).node))  # 1->4->2->3.
    print(s.reorderList(LinkedList([1, 2, 3, 4, 5]).node))  # 1->5->2->4->3