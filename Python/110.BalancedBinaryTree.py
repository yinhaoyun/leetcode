# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def depth(node) -> int:
            if not node:
                return 0
            l = depth(node.left)
            if l == -1: return -1
            r = depth(node.right)
            if r == -1: return -1

            if abs(l - r) > 1: return -1
            return 1 + max(l, r)

        return depth(root) != -1

    def isBalanced_top_down(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        def depth(node) -> int:
            if not node: return 0
            return 1 + max(depth(node.left), depth(node.right))

        return abs(depth(root.left) - depth(root.right)) <= 1 and \
               self.isBalanced(root.left) and \
               self.isBalanced(root.right)
