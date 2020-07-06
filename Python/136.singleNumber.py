from typing import List


# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for n in nums:
            result ^= n
        return result


s = Solution()
print(s.singleNumber([2, 2, 1]))  # 1
print(s.singleNumber([4, 1, 2, 1, 2]))  # 4
print(s.singleNumber([0, 1, 0]))  # 1
print(s.singleNumber([2, 2, 1]))  # 1
print(s.singleNumber([1, 3, 1, -1, 3]))  # -1
print(s.singleNumber([17,12,5,-6,12,4,17,-5,2,-3,2,4,5,16,-3,-4,15,15,-4,-5,-6]))  # 16