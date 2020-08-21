from typing import List


# https://leetcode.com/problems/sort-array-by-parity/
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return [a for a in A if a % 2 == 0] + [a for a in A if a % 2 == 1]


if __name__ == '__main__':
    s = Solution()
    print(s.sortArrayByParity([3,1,2,4]))