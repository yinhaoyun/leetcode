import copy
import itertools
from typing import List

"""
Given a collection of distinct integers, return all possible permutations.

"""
class Solution:
    def __init__(self):
        self.permute = self.back_tracking

    def back_tracking(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(n: int):
            if n == len(nums) - 1:
                res.append(copy.copy(nums))
                return
            for i in range(n, len(nums)):
                nums[i], nums[n] = nums[n], nums[i]
                helper(n + 1)
                nums[i], nums[n] = nums[n], nums[i]

        helper(0)
        return res

    def built_in(self, nums: List[int]) -> List[List[int]]:
        """Cheat but fast"""
        return [list(i) for i in itertools.permutations(nums)]

    def picked_flag(self, nums: List[int]) -> List[List[int]]:
        """Use picked flag, slow when the list is long"""
        res = []
        picked = [False] * len(nums)

        def helper(formed: List[int]):
            if len(formed) == len(nums):
                res.append(formed)
                return
            for i, n in enumerate(nums):
                if not picked[i]:
                    picked[i] = True
                    helper(formed + [nums[i]])
                    picked[i] = False
        helper([])
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.permute([1, 2, 3]))