from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join([str(x) for x in digits])) + 1
        return [c for c in str(num)]

s = Solution()
print(s.plusOne( [1,2,3]))  # 124
print(s.plusOne( [4,3,2,1]))  # 4322
print(s.plusOne( [4,3,2,9]))  # 4330
print(s.plusOne( [9,9,9,9]))  # 10000