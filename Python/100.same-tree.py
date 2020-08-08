from data_structure.BinaryTree import BinaryTree
from data_structure.TreeNode import TreeNode


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # print(p, q)
        if p and not q or not p and q:
            return False
        if not p and not q:
            return True
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


s = Solution()
tree1 = BinaryTree([1, 2, 3])
tree2 = BinaryTree([1, 2, 3])
print(s.isSameTree(tree1.root, tree2.root))  # True
tree1 = BinaryTree([1, 2])
tree2 = BinaryTree([1,None,2])
print(s.isSameTree(tree1.root, tree2.root))  # False
tree1 = BinaryTree([1,2,1])
tree2 = BinaryTree([1,1,2])
print(s.isSameTree(tree1.root, tree2.root))  # False
