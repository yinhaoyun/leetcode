from data_structure.tree_node import TreeNode
from data_structure.binary_tree import BinaryTree


# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        if not root:
            return 0
        result = 0
        def helper(node: TreeNode, formed: int) -> None:
            nonlocal  result
            formed = formed * 2 + node.val
            if not node.left and not node.right:
                result += formed
            if node.left:
                helper(node.left, formed)
            if node.right:
                helper(node.right, formed)

        helper(root, 0)
        return result


if __name__ == "__main__":
    s = Solution()
    bt = BinaryTree([1,0,1,0,1,0,1])
    print(s.sumRootToLeaf(bt.root))