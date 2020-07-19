import collections
from collections import defaultdict
from typing import List


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        g = defaultdict(list)
        res = [0] * n
        for p, c in edges:
            g[p] += [c]
            g[c] += [p]

        def dfs(node: int, parent: int) -> int:
            cnt = collections.Counter()
            cnt[labels[node]] += 1
            for child in g.get(node):
                if child != parent:
                    cnt += dfs(child, node)
            res[node] = cnt[labels[node]]
            return cnt
        dfs(0, -1)

        return res

s = Solution()

print(s.countSubTrees(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], labels = "abaedcd")) # [2,1,1,1,1,1,1]
print(s.countSubTrees(n = 4, edges = [[0,1],[1,2],[0,3]], labels = "bbbb"))  # [4,2,1,1]
print(s.countSubTrees(n = 5, edges = [[0,1],[0,2],[1,3],[0,4]], labels = "aabab"))  # [3,2,1,1,1]
print(s.countSubTrees(n = 6, edges = [[0,1],[0,2],[1,3],[3,4],[4,5]], labels = "cbabaa"))  # [1,2,1,1,2,1]
print(s.countSubTrees(n = 7, edges = [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6]], labels = "aaabaaa"))  # [6,5,4,1,3,2,1]
print(s.countSubTrees(4, [[0,2],[0,3],[1,2]], "aeed"))