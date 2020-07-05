from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        # print(grid)
        z_count = 0
        y_count = 0
        x_count = 0
        x_max = [0] * len(grid[0])
        for i in range(len(grid)):
            y_count += max(grid[i])
            for j in range(len(grid[0])):
                if grid[i][j]:
                    z_count += 1
                    x_max[j] = max(grid[i][j], x_max[j])
        x_count = sum(x_max)


        # print(z_count, y_count, x_count)
        return z_count + y_count + x_count



s = Solution()
print(s.projectionArea([[2]]))  # 5
print(s.projectionArea([[1,2],[3,4]]))  # 17
print(s.projectionArea([[1,0],[0,2]]))  # 8
print(s.projectionArea([[1,1,1],[1,0,1],[1,1,1]]))  # 14
print(s.projectionArea([[2,2,2],[2,1,2],[2,2,2]]))  # 21