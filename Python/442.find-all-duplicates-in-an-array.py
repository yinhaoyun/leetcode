from typing import List

# TODO: Improve algorithm
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = set()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                res.add(nums[i])
        return list(res)


s = Solution()
print(s.findDuplicates([4,3,2,7,8,2,3,1]))