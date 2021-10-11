# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        def min_depth(node) -> int:
            if not node: return 0
            if not node.right and not node.left: return 1
            left = min_depth(node.left)
            right = min_depth(node.right)
            if not node.right: return 1 + left
            if not node.left: return 1 + right
            return 1 + min(left, right)

        ans = min_depth(root)
        return ans
