from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        layer_array = []

        def dfs(node: TreeNode, depth: int) -> None:
            if node is None:
                return
            if depth > len(layer_array) - 1:
                layer_array.append([])
            layer_array[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        for i in range(1, len(layer_array), 2):
            layer_array[i].reverse()
        return layer_array


s = Solution()
print(s.zigzagLevelOrder(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
