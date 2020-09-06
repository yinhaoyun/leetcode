from typing import List


# https://leetcode.com/problems/matrix-diagonal-sum/
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        N = len(mat)
        out = sum([mat[i][i] for i in range(N)]) + sum([mat[N - i - 1][i] for i in range(N)])
        if N % 2:
            out -= mat[N//2][N//2]
        return out


if __name__ == "__main__":
    s = Solution()
    print(s.diagonalSum([[1,2,3],
                  [4,5,6],
                  [7,8,9]]))  # 25
    print(s.diagonalSum([[1,1,1,1],
                  [1,1,1,1],
                  [1,1,1,1],
                  [1,1,1,1]]))  # 8
    print(s.diagonalSum([[5]]))  # 5