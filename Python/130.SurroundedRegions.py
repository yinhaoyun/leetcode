from typing import List


class Solution:
    DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        CY, CX = len(board), len(board[0])
        for y in range(CY):
            for x in range(CX):
                if board[y][x] == 'O':
                    board[y][x] = '#'

        def dfs(y, x):
            if board[y][x] != '#':
                return
            board[y][x] = 'O'
            for dy, dx in Solution.DIRS:
                ny, nx = y + dy, x + dx
                if not (0 <= ny < CY) or not (0 <= nx < CX):
                    continue
                dfs(ny, nx)

        for y in range(CY):
            dfs(y, 0)
            dfs(y, CX - 1)

        for x in range(CX):
            dfs(0, x)
            dfs(CY - 1, x)

        for y in range(CY):
            for x in range(CX):
                if board[y][x] == '#':
                    board[y][x] = 'X'


