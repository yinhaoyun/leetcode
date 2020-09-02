from bisect import bisect_left, bisect_right

from sortedcontainers import SortedList
from typing import List


# https://leetcode.com/problems/contains-duplicate-iii/
class Solution:
    def __init__(self):
        self.containsNearbyAlmostDuplicate = self.sorted_list

    def sorted_list(self, nums: List[int], k: int, t: int) -> bool:
        slist = SortedList()
        for i in range(len(nums)):
            if i > k:
                slist.remove(nums[i-k-1])
            pos1 = bisect_left(slist, nums[i] - t)
            pos2 = bisect_right(slist, nums[i] + t)
            if pos1 != pos2 and pos1 != len(slist):
                return True
            slist.add(nums[i])
        return False

    def simple(self, nums: List[int], k: int, t: int) -> bool:
        k = min(k, len(nums) - 1)
        for i in range(len(nums) - k):
            sorted_nums = sorted(nums[i:i+k+1])
            print(sorted_nums)
            for j in range(len(sorted_nums) - 1):
                if abs(sorted_nums[j] - sorted_nums[j+1]) <= t:
                    return True
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.containsNearbyAlmostDuplicate(nums = [1,2,3,1], k = 3, t = 0))  # True
    print(s.containsNearbyAlmostDuplicate(nums = [1,0,1,1], k = 1, t = 2))  # True
    print(s.containsNearbyAlmostDuplicate(nums = [1,5,9,1,5,9], k = 2, t = 3))  # False
    print(s.containsNearbyAlmostDuplicate([2, 2], 3, 0)) # True
