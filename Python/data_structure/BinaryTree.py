import collections
from typing import List

from data_structure.TreeNode import TreeNode


class BinaryTree:
    def __init__(self, tree_values: List, skip_none_children=False):
        if len(tree_values) == 0:
            raise ValueError
        print(tree_values)
        self.root = TreeNode()
        queue = collections.deque([])
        queue.append(self.root)
        tree_nodes = [TreeNode(value) if value is not None else None for value in tree_values]
        if skip_none_children:
            print("skip_none_children: extend tree_nodes")
            i = 0
            while i < len(tree_values):
                if tree_nodes[i] is None:
                    left_index = i * 2 + 1
                    if left_index < len(tree_nodes) - 1:
                        tree_nodes.insert(left_index, None)
                        print(tree_nodes)
                    right_index = i * 2 + 2
                    if right_index < len(tree_nodes) - 1:
                        tree_nodes.insert(right_index, None)
                        print(tree_nodes)
                i += 1
            print("extend tree_nodes: ", tree_nodes)

        for i, node in enumerate(tree_nodes):
            left_index = i * 2 + 1
            if left_index < len(tree_nodes) and tree_nodes[left_index]:
                node.left = tree_nodes[left_index]
            right_index = i * 2 + 2
            if right_index < len(tree_nodes) and tree_nodes[right_index]:
                node.right = tree_nodes[right_index]
        self.root = tree_nodes[0]

    def __repr__(self):
        repr = "BinaryTree:"
        q = collections.deque([self.root])
        while len(q):
            for n in list(q):
                repr += str(n.val)
                q.popleft()
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
        return repr
