# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        def dfsSum(root: TreeNode, cur_sum: int):
            cur_sum += root.val
            if not root.left and not root.right:
                if cur_sum == sum:
                    return True
            else:
                if root.left and dfsSum(root.left, cur_sum):
                    return True
                if root.right and dfsSum(root.right, cur_sum):
                    return True

        return dfsSum(root, 0)
