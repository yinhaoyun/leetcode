from typing import List


# https://leetcode.com/problems/pascals-triangle/
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(1, numRows+1):
            result.append([1] * i)
            if i <= 2:
                continue
            for j in range(1, i-1):
                result[-1][j] = result[-2][j-1] + result[-2][j]
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.generate(0))
    print(s.generate(5))