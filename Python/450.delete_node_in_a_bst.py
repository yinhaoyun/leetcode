from data_structure.binary_tree import BinaryTree
from data_structure.tree_node import TreeNode


# https://leetcode.com/problems/delete-node-in-a-bst/
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left or not root.right:
                root = root.left if root.left else root.right
            else:
                cur = root.right
                while cur.left:
                    cur = cur.left
                root.val = cur.val
                root.right = self.deleteNode(root.right, cur.val)
        return root


if __name__ == "__main__":
    s = Solution()
    tree = BinaryTree([5, 3, 6, 2, 4, None, 7])
    s.deleteNode(tree.root, 3)
    print(tree)