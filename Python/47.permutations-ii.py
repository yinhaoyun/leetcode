from typing import List


class Solution:
    def __init__(self):
        self.permuteUnique = self.back_tracking

    def back_tracking(self, nums: List[int]) -> List[List[int]]:
        def helper(nums: List[int], formed: List[int]) -> None:
            if not nums:
                res.append(formed)
            picked = []
            for i, n in enumerate(nums):
                if n not in picked:
                    helper(nums[:i] + nums[i+1:], formed + [n])
                    picked.append(n)

        res = []
        helper(nums, [])
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.permuteUnique([1,1,2]))