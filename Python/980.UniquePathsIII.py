from typing import List


class Solution:
    OBSTACLE, EMPTY, END, START, USED = range(-1, 4)
    DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        CY, CX = len(grid), len(grid[0])
        empty_cnt = 0
        start, end = (0, 0), (0, 0)
        for y in range(CY):
            for x in range(CX):
                if grid[y][x] == Solution.EMPTY:
                    empty_cnt += 1
                elif grid[y][x] == Solution.START:
                    start = y, x
                elif grid[y][x] == Solution.END:
                    end = y, x

        def dfs(y, x, empty_cnt):
            nonlocal end
            if (y, x) == end:
                return 0 if empty_cnt != -1 else 1
            grid[y][x] = Solution.USED

            total = 0
            for dy, dx in Solution.DIRS:
                ny, nx = y + dy, x + dx
                if not 0 <= ny < CY or not 0 <= nx < CX or grid[ny][nx] in [Solution.START, Solution.OBSTACLE,
                                                                            Solution.USED]:
                    continue
                total += dfs(ny, nx, empty_cnt - 1)
            grid[y][x] = Solution.EMPTY
            return total

        return dfs(*start, empty_cnt)


