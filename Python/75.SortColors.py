from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i, j, k = 0, 0, len(nums) - 1
        while j <= k:
            if nums[j] < 1:
                nums[i], nums[j] = nums[j], nums[i]
                i, j = i + 1, j + 1
            elif nums[j] > 1:
                nums[k], nums[j] = nums[j], nums[k]
                k -= 1
            else:
                j += 1
