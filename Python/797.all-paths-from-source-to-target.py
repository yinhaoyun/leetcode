from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(formed: List[int]) -> None:
            if formed[-1] == (n - 1):
                sol.append(formed)
                return
            for i in graph[formed[-1]]:
                dfs(formed + [i])

        sol, n = [], len(graph)
        dfs([0])
        return sol


s = Solution()
print(s.allPathsSourceTarget([[1, 2], [3], [3], []]))  # [[0,1,3],[0,2,3]]
