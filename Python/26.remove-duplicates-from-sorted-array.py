from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # two pointer
        i, j = 0, 1
        while j < len(nums):
            while nums[i] == nums[j]:
                j += 1
                if j >= len(nums):
                    return i + 1
            i += 1
            nums[i] = nums[j]
            j += 1
        return i + 1


s = Solution()
print(s.removeDuplicates([1]))  # 1
print(s.removeDuplicates([1,1]))  # 1
print(s.removeDuplicates([1,2]))  # 2
print(s.removeDuplicates([1,1,2]))  # 2
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))  # 5