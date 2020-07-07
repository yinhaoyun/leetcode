from typing import List




class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0

        def count_edge(x, y):
            edge = 0
            if x == 0 or grid[y][x-1] == 0:
                edge += 1
            if x == len(grid[0])-1 or grid[y][x+1] == 0:
                edge += 1
            if y == 0 or grid[y-1][x] == 0:
                edge += 1
            if y == len(grid)-1 or grid[y+1][x] == 0:
                edge += 1
            return edge

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x]:
                    res += count_edge(x, y)
        return res


s = Solution()
print(s.islandPerimeter([[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]
))  # 16

print(s.islandPerimeter([[0,1,0,0],
 [0,0,0,0],
 [0,0,0,0],
 [0,0,0,0]]
))  # 4

print(s.islandPerimeter([[0,0,0,0],
                         [0,0,0,0],
                         [0,0,0,0],
                         [0,0,1,1]]
                        ))  # 6

print(s.islandPerimeter([[0,0,0,0],
                         [0,0,0,0],
                         [0,0,1,0],
                         [0,0,0,0]]
                        ))  # 4