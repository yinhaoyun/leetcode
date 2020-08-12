from typing import List


# https://leetcode.com/problems/pascals-triangle-ii/
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1] * (rowIndex+1)
        for r in range(1, rowIndex+1):
            result[r] = (result[r-1] * (rowIndex - r + 1)) // r
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.getRow(3))
    print(s.getRow(4))
    print(s.getRow(5))