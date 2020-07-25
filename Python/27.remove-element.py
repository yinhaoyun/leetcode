from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            if nums[start] == val:
                nums[start], nums[end], end = nums[end], nums[start], end - 1
            else:
                start += 1
        return start


s = Solution()
print(s.removeElement([1], val=1))  # 0
print(s.removeElement([3, 2, 2, 3], val=4))  # 4
print(s.removeElement([3, 2, 2, 3], val=3))  # 2
print(s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], val=2))  # 5
