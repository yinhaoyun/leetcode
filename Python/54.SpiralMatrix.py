from typing import List


class Solution:
    def spiralOrder(self, matrix):
        n, m = len(matrix[0]), len(matrix)
        x, y, dx, dy = 0, 0, 1, 0
        ans = []
        for _ in range(m * n):
            if not 0 <= x + dx < n or not 0 <= y + dy < m or matrix[y + dy][x + dx] == "*":
                dx, dy = -dy, dx

            ans.append(matrix[y][x])
            matrix[y][x] = "*"
            x, y = x + dx, y + dy

        return ans
    # my answer: 16.96% BAD
    def spiralOrder_my(self, matrix: List[List[int]]) -> List[int]:
        CY, CX = len(matrix), len(matrix[0])
        N = CX * CY
        if CY == 1: return matrix[0]
        if CX == 1: return [l[0] for l in matrix]
        x, y = 0, 0
        RIGHT, BOTTOM, LEFT, TOP = 0, 1, 2, 3
        bounds = [CX - 1, CY - 1, 0, 0]  # right, bottom, left, top

        def in_bounds(x, y) -> bool:
            nonlocal bounds
            print(f"in_bounds: bounds={bounds}, x={x}, y={y}, dir={dir}")
            if not bounds[LEFT] <= x <= bounds[RIGHT]:
                return False
            elif not bounds[TOP] <= y <= bounds[BOTTOM]:
                return False
            return True

        ans = [0] * N

        index = 0

        DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)] # ->, v, <-, ^
        ans[0] = matrix[0][0]
        while True:
            for dir, (dx, dy) in enumerate(DIRS):
                print(f"dir={dir}, dx, dy=[{dx}, {dy}]")
                while in_bounds(x + dx, y + dy):
                    x, y = x + dx, y + dy
                    index += 1
                    print(f"({x}, {y})")
                    print(f"ans[{index}] = {matrix[y][x]}")
                    ans[index] = matrix[y][x]
                    if index == len(ans) - 1:
                        return ans
                p_dir = (dir - 1) % len(DIRS)
                bounds[p_dir] += (1 if p_dir in [LEFT, TOP] else -1)
                print(f"update bounds={bounds}")
                print(f"index = {index}")
                print(f"ans = {ans}")

if __name__ == "__main__":
    s = Solution()
    print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])) # [1,2,3,6,9,8,7,4,5]
    print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])) # [1,2,3,4,8,12,11,10,9,5,6,7]

