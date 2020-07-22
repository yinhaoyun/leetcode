from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        layer_array = []

        def dfs(node: TreeNode, depth: int) -> None:
            if depth > len(layer_array) - 1:
                layer_array.append([])
            layer_array[depth].append(node.val)
            if node.left:
                dfs(node.left, depth + 1)
            if node.right:
                dfs(node.right, depth + 1)
        if root:
            dfs(root, 0)
        return layer_array


s = Solution()
print(s.levelOrder(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
