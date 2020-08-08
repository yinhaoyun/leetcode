from typing import List

from data_structure.linked_list import LinkedList
from data_structure.list_node import ListNode


class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        length = 0
        p = root
        while p:
            length += 1
            p = p.next
        result = [None] * k
        per_size = length // k
        padding = length % k

        p = root
        i = 0
        while p:
            result[i] = p
            i += 1
            size = per_size + 1 if padding > 0 else per_size
            prev = None
            while size > 0:
                prev = p
                p = p.next
                size -= 1
            padding -= 1
            prev.next = None
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.splitListToParts(root = LinkedList([1, 2, 3]).node, k = 5))  # [[1],[2],[3],[],[]]
    print(s.splitListToParts(root = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).node, k = 3))  # [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
