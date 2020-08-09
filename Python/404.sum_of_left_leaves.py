from data_structure.binary_tree import BinaryTree
from data_structure.tree_node import TreeNode


class Solution:
    """
    https://leetcode.com/problems/sum-of-left-leaves/
    """
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        res = 0
        if root and root.left:
            if not root.left.left and not root.left.right:
                res += root.left.val
            res += self.sumOfLeftLeaves(root.left)
        if root and root.right:
            res += self.sumOfLeftLeaves(root.right)
        return res


if __name__ == '__main__':
    s = Solution()
    tree = BinaryTree([3, 9, 20, None, None, 15, 7], skip_none_children=False)
    print(s.sumOfLeftLeaves(tree.root))
    tree = BinaryTree([1,2,3,4,5])
    print(s.sumOfLeftLeaves(tree.root))