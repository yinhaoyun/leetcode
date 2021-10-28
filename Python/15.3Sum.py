from collections import Counter
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            lo, hi, target = i + 1, len(nums) - 1, -nums[i]
            while lo < hi:
                if nums[lo] + nums[hi] == target:
                    ans.append([nums[i], nums[lo], nums[hi]])
                    lo, hi = lo + 1, hi - 1
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi + 1]:
                        hi -= 1
                elif nums[lo] + nums[hi] < target:
                    lo += 1
                else:
                    hi -= 1

        return ans
