# 922. Sort Array By Parity II

from typing import List

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        inde, indo = 0, 1
        n = len(nums)
        while True:
            while inde < n and nums[inde] % 2 == 0:
                inde += 2
            if inde >= n: break
            while indo < n and nums[indo] % 2 == 1:
                indo += 2
            if indo >= n: break
            nums[inde], nums[indo] = nums[indo], nums[inde]
        return nums


s = Solution()
print(s.sortArrayByParityII([4,2,5,7,8,9]))