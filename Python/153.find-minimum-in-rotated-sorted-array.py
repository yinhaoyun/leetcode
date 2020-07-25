from typing import List


class Solution:
    """
    https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
    Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
    (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
    Find the minimum element.
    You may assume no duplicate exists in the array.
    """

    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        start, end = 0, len(nums) - 1
        while True:
            if start + 1 >= end:
                return nums[end]
            mid = (start + end) // 2
            if nums[start] > nums[mid]:
                end = mid
            elif nums[mid] > nums[end]:
                start = mid



if __name__ == '__main__':
    s = Solution()
    print(s.findMin([1]))  # 1
    print(s.findMin(list(range(5))))  # 0
    print(s.findMin(list(range(101))))  # 0
    print(s.findMin([3, 4, 5, 1, 2]))  # 1
    print(s.findMin([3, 4, 5, 1, 2]))  # 1
    print(s.findMin([4, 5, 6, 7, 0, 1, 2]))  # 0
    print(s.findMin([3, 4, 5, 6, 7, 0, 1, 2]))  # 0
    print(s.findMin([3, 4, 5, 6, 7, 1, 2]))  # 0
