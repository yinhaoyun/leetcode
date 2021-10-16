# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # merkle tree
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        from hashlib import sha256
        def hash(data: str):
            s = sha256()
            s.update(data.encode('ascii'))
            return s.hexdigest()
        def merkle(node):
            if not node:
                return "_"
            node.merkle = hash(merkle(node.left) + str(node.val) + merkle(node.right))
            return node.merkle
        merkle(root)
        merkle(subRoot)

        def dfs(node) -> bool:
            nonlocal subRoot
            if not node:
                return False
            return node.merkle == subRoot.merkle or \
                    dfs(node.left) or dfs(node.right)
        return dfs(root)


    def isSubtree_compare_whole_tree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def is_same(p, q) -> bool:
            if not p and not q: return True
            if not p or not q: return False
            if p.val != q.val: return False
            return is_same(p.left, q.left) and is_same(p.right, q.right)

        def traverse(node, subRoot) -> bool:
            if not node: return False
            return is_same(node, subRoot) or \
                   traverse(node.left, subRoot) or \
                   traverse(node.right, subRoot)

        return traverse(root, subRoot)