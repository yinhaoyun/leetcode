# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def is_symmetric(root1, root2) -> bool:
            if not root1 and not root2: return True
            if not root1 or not root2: return False
            return root1.val == root2.val and is_symmetric(root1.left, root2.right) and is_symmetric(root1.right,
                                                                                                     root2.left)

        return is_symmetric(root.left, root.right)
