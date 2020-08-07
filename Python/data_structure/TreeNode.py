import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        repr = "TreeNode:"
        q = collections.deque([self])
        while len(q):
            for n in list(q):
                repr += str(n.val)
                q.popleft()
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
        return repr