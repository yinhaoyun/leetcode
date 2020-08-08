import collections
from typing import List

from data_structure.binary_tree import BinaryTree
from data_structure.tree_node import TreeNode


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        verticals = collections.defaultdict(list)

        # in-order traversal and record the x,y
        def helper(x: int, y: int, node: TreeNode):
            if not node:
                return
            verticals[x].append((y, node.val))
            helper(x - 1, y + 1, node.left)
            helper(x + 1, y + 1, node.right)

        helper(0, 0, root)
        ret = []
        for key in sorted(verticals.keys()):
            ret.append([v[1] for v in sorted(verticals[key])])
        return ret


if __name__ == '__main__':
    s = Solution()
    tree = BinaryTree([3, 9, 20, None, None, 15, 7], skip_none_children=True)
    print(tree)
    print(s.verticalTraversal(tree.root))  # [[9],[3,15],[20],[7]]

    tree = BinaryTree([1, 2, 3, 4, 5, 6, 7], skip_none_children=True)
    print(tree)
    print(s.verticalTraversal(tree.root))  # [[4],[2],[1,5,6],[3],[7]]

    tree = BinaryTree([1, None, 3, 4, 5], skip_none_children=True)
    print(tree)
    print(s.verticalTraversal(tree.root))  # [[1, 4], [3], [5]]

    tree = BinaryTree([0,8,1,None,None,3,2,None,4,5,None,None,7,6], skip_none_children=True)
    print(tree)
    print(s.verticalTraversal(tree.root))  # [[8], [0, 3, 6], [1, 4, 5], [2, 7]]
