import collections
from typing import List

from .tree_node import TreeNode


class BinaryTree:
    def __init__(self, values: List, skip_none_children=False):
        if values is None or len(values) == 0:
            raise ValueError("values is None or length = 0")
        # print(values)
        self.root = TreeNode(values[0])
        q = collections.deque([self.root])

        i = 1
        while len(q) > 0 and i < len(values):
            # print(q)
            node = q.popleft()
            if i < len(values) and values[i] is not None:
                node.left = TreeNode(values[i])
            if node and (node.left or not skip_none_children):
                q.append(node.left)

            i += 1
            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])

            if node and (node.right or not skip_none_children):
                q.append(node.right)
            i += 1

    def __repr__(self):
        q = collections.deque([self.root])
        heap = []
        while len(q) and q.count(None) != len(q):
            n = q.popleft()
            if n:
                heap.append(n.val)
                q.append(n.left)
                q.append(n.right)
            else:
                heap.append(None)
                q.append(None)
                q.append(None)

        return f"BinaryTree: [{', '.join([str(e) for e in heap])}]"


if __name__ == '__main__':
    tree = BinaryTree([3, 9, 20, None, None, 15, 7], skip_none_children=True)
    print(tree)  # [3, 9, 20, None, None, 15, 7]

    tree = BinaryTree([1, 2, 3, 4, 5, 6, 7], skip_none_children=True)
    print(tree)  # [1, 2, 3, 4, 5, 6, 7]

    tree = BinaryTree([1, None, 3, 4, 5], skip_none_children=True)
    print(tree)  # [1, None, 3, None, None, 4, 5]
    tree = BinaryTree([1, None, 3, None, None, 4, 5])
    print(tree)  # [1, None, 3, None, None, 4, 5]
