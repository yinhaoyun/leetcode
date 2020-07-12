from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            res += nums[i+1:].count(nums[i])
        return res



s = Solution()
print(s.numIdenticalPairs([1,2,3,1,1,3]))  # 4
print(s.numIdenticalPairs( [1,1,1,1]))  # 6
print(s.numIdenticalPairs( [1,2,3]))  # 0