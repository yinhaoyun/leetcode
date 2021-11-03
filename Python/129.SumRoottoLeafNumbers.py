from typing import List


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def tree_values(root) -> List[int]:
            if not root: return []
            if not root.left and not root.right:
                return [str(root.val)]
            return [str(root.val) + v for v in tree_values(root.left) + tree_values(root.right)]

        return sum(int(v) for v in tree_values(root))

