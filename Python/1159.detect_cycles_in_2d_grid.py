import itertools
from typing import List


# TODO: https://leetcode.com/problems/detect-cycles-in-2d-grid/discuss/805691/Clean-Python-3-Union-and-Find
# https://leetcode.com/problems/detect-cycles-in-2d-grid/
class Solution:
    DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))

    # https://leetcode.com/problems/detect-cycles-in-2d-grid/discuss/805677/DFS-or-Simple-Explanation
    # Runtime: 4428 ms, faster than 7.14%
    def containsCycle(self, grid: List[List[str]]) -> bool:
        # print(f"containsCycle: grid={grid}")
        cy, cx = len(grid), len(grid[0])
        visited = set()
        visited = [[False] * cx for _ in range(cy)]

        def dfs(x: int, y: int, last_x: int = -1, last_y: int = -1) -> bool:
            visited[y][x] = True

            # print(f"enter dfs: symbol={symbol}, coord={x, y}, last coord={last_x, last_y}")
            # print(f"all dirs: {[(x + dx, y + dy) for dx, dy in Solution.DIRS]}")
            # print(f"dirs={dirs}")
            for nx, ny in filter(lambda coord: (coord[0] != last_x or coord[1] != last_y) and (0 <= coord[0] < cx) and (0 <= coord[1] < cy), [(x + dx, y + dy) for dx, dy in Solution.DIRS]):
                # print(f"search coord={nx, ny}")
                if grid[ny][nx] == symbol:
                    if visited[ny][nx] or dfs(nx, ny, x, y):
                        # print(f"True: coord={nx, ny}, visited={visited[ny][nx]}")
                        return True
            # print(f"leave dfs: symbol={symbol}, coord={x, y}, last coord={last_x, last_y}")
            return False

        for y, x in itertools.product(range(cy), range(cx)):
            if not visited[y][x]:
                symbol = grid[y][x]
                # print(f"call dfs: symbol={symbol}, coord={x, y}")
                if dfs(x, y):
                    return True
        return False


s = Solution()
print(s.containsCycle(
    grid=[["a", "a", "a", "a"], ["a", "b", "b", "a"], ["a", "b", "b", "a"], ["a", "a", "a", "a"]]))  # True
print(s.containsCycle(
    grid=[["c", "c", "c", "a"], ["c", "d", "c", "c"], ["c", "c", "e", "c"], ["f", "c", "c", "c"]]))  # True
print(s.containsCycle(grid=[["a", "b", "b"], ["b", "z", "b"], ["b", "b", "a"]]))  # False
print(s.containsCycle([["b","a","c"],["c","a","c"],["d","d","c"],["b","c","c"]]))