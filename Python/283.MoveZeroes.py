class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        i, j = 0, 0

        while j < N:
            if nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1