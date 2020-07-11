from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(comb: List[int], n: int):
            if n == len(nums):
                # print(comb)
                res.append(list(comb))
                return

            # pick
            comb.append(nums[n])
            helper(comb, n+1)
            comb.pop()
            helper(comb, n+1)
            # not pick

        helper([], 0)
        return res



s = Solution()
print(s.subsets(nums = [1,2,3]))