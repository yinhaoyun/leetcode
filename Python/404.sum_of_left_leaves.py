from collections import deque

from data_structure.binary_tree import BinaryTree
from data_structure.tree_node import TreeNode

class Solution:
    """
    https://leetcode.com/problems/sum-of-left-leaves/
    """
    def recursive_dfs(self, root: TreeNode) -> int:
        res = 0
        if root and root.left:
            if not root.left.left and not root.left.right:
                res += root.left.val
            res += self.sumOfLeftLeaves(root.left)
        if root and root.right:
            res += self.sumOfLeftLeaves(root.right)
        return res

    # queue
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        result, lefts, others = 0, deque([]), deque([root])

        def left_or_others(q: deque) -> None:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    lefts.append(node.left)
                if node.right:
                    others.append(node.right)

        while lefts or others:
            result += sum([n.val for n in lefts if not n.left and not n.right])
            left_or_others(lefts)
            left_or_others(others)
        return result


if __name__ == '__main__':
    s = Solution()
    tree = BinaryTree([3, 9, 20, None, None, 15, 7], skip_none_children=False)
    print(s.sumOfLeftLeaves(tree.root))  # 24
    tree = BinaryTree([1,2,3,4,5])
    print(s.sumOfLeftLeaves(tree.root))  # 4
