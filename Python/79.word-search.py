from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        cy = len(board)
        cx = len(board[0])
        seen = [[0 for x in range(cx)] for i in range(cy)]
        # print(board, seen, word)

        def dfs(x: int, y: int, cur: int) -> bool:
            # print("dfs", x, y, cur, word[cur], board[y][x], seen)
            if seen[y][x] == 1 or cur >= len(word) or word[cur] != board[y][x]:
                # if seen[y][x] == 1:
                #     print("seen[y][x] == 1")
                # if cur >= len(word):
                #     print("cur >= len(word)")
                # if word[cur] != board[y][x]:
                #     print("word[cur] != board[y][x]")
                return False
            if cur == len(word) - 1:
                return True
            seen[y][x] = 1
            if (x < cx - 1 and dfs(x + 1, y, cur + 1)) or \
                    (y < cy - 1 and dfs(x, y + 1, cur + 1)) or \
                    (x > 0 and dfs(x - 1, y, cur + 1)) or \
                     (y > 0 and dfs(x, y - 1, cur + 1)):
                return True
            seen[y][x] = 0
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
