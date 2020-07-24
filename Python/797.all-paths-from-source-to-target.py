from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        path = dict()
        j = len(graph) - 1

        def find_path(i: int) -> List[int]:
            if path.get(i):
                pass
            elif i == j:  # end
                path[i] = [[i]]
                # print(i, path[i])
            else:
                path[i] = []
                for n in graph[i]:
                    ext_path = find_path(n)
                    if ext_path:
                        for p in ext_path:
                            path[i].append([i] + p)
                # print(i, path[i])
            return path[i]

        return find_path(0)


s = Solution()
print(s.allPathsSourceTarget([[1, 2], [3], [3], []]))  # [[0,1,3],[0,2,3]]
