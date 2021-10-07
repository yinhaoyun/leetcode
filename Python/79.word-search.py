from typing import List


class Solution:
    DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def exist(self, board: List[List[str]], word: str) -> bool:
        n_r, n_c, n_w = len(board), len(board[0]), len(word)
        is_visited = [[0] * n_c for _ in range(n_r)]

        def dfs(y: int, x: int, d: int) -> bool:
            nonlocal board, word, n_r, n_c, n_w, is_visited
            if not (0 <= y < n_r and 0 <= x < n_c) or is_visited[y][x] or board[y][x] != word[d]:
                return False

            if d == n_w - 1:
                return True
            is_visited[y][x] = True
            for dy, dx in Solution.DIRS:
                if dfs(y + dy, x + dx, d + 1):
                    return True

            is_visited[y][x] = False
            return False

        for y in range(n_r):
            for x in range(n_c):
                if dfs(y, x, 0):
                    return True

        return False

        for y, r in enumerate(board):
            for x, c in enumerate(r):
                # print(x, y)
                if dfs(x, y, 0):
                    return True
        return False


s = Solution()
board = [['A', 'B', 'C', 'E'],
         ['S', 'F', 'C', 'S'],
         ['A', 'D', 'E', 'E']]
print(s.exist(board, word="ABCCED"))  # true
print(s.exist(board, word="SEE"))  # true
print(s.exist(board, word="ABCB"))  # false
