from functools import lru_cache
from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        tgt_sum, remain = divmod(sum(nums), k)
        if remain or max(nums) > tgt_sum:
            return False
        n = len(nums)
        nums.sort(reverse=True)

        def dp(mask, cur, memo) -> bool:
            if mask == 0:
                return cur == 0
            elif cur == 0:
                return dp(mask, sum(nums) / k, memo)
            if (mask, cur) not in memo:
                res = False
                for bit in range(n):
                    if mask & (1 << bit):
                        if nums[bit] > cur:
                            continue
                        if (dp(mask ^ (1 << bit), cur - nums[bit], memo)):
                            res = True
                            break
                memo[(mask, cur)] = res
            return memo[(mask, cur)]

        return dp(2**n-1, sum(nums) // k, dict())

s = Solution()
print(s.canPartitionKSubsets(nums=[4, 3, 2, 3, 5, 2, 1], k=4))  # True
print(s.canPartitionKSubsets(nums=[1, 2, 3, 4], k=3))  # False
print(s.canPartitionKSubsets([815,625,3889,4471,60,494,944,1118,4623,497,771,679,1240,202,601,883], 3))