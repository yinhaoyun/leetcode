from typing import List

from Python.data_structure.binary_tree import BinaryTree
from Python.data_structure.tree_node import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.pathSum = self.short_dfs

    def short_dfs(self, root: TreeNode, target_sum: int) -> int:
        def dfs(node: TreeNode, sums: List[int]) -> int:
            if not node:
                return 0
            sums = [s + node.val for s in sums] + [node.val]
            res = sums.count(target_sum)
            res += dfs(node.left, sums) if node.left else 0
            res += dfs(node.right, sums) if node.right else 0
            return res
        return dfs(root, [])

    def simple_dfs(self, root: TreeNode, target_sum: int) -> int:

        def dfs(node: TreeNode, sums: List[int]) -> None:
            nonlocal target_sum
            nonlocal res
            if not node:
                return
            sums = [s + node.val for s in sums] + [node.val]
            res += sums.count(target_sum)
            if node.left:
                dfs(node.left, sums)
            if node.right:
                dfs(node.right, sums)
        res = 0
        dfs(root, [])
        return res


if __name__ == '__main__':
    s = Solution()
    tree = BinaryTree([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
    print(tree)
    print(s.pathSum(tree.root, 8))  # 3
    print(s.pathSum(None, 1))  # 0
