# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def is_flip_equiv(p, q) -> bool:
            if not p and not q: return True
            if not p or not q: return False
            if p.val != q.val: return False
            return (is_flip_equiv(p.left, q.left) and is_flip_equiv(p.right, q.right)) or (
                        is_flip_equiv(p.left, q.right) and is_flip_equiv(p.right, q.left))

        return is_flip_equiv(root1, root2)