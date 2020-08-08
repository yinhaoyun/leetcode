from typing import List

"""
https://leetcode.com/contest/biweekly-contest-32/problems/kth-missing-positive-number/
"""
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arr2 = [0] + arr[:-1]
        missing_arr =  list(map(lambda x, y: x - y - 1, arr, arr2))
        print(missing_arr)
        for i, n in enumerate(missing_arr):
            if k - n <= 0:
                if i == 0:
                    return k
                else:
                    return arr[i - 1] + k
            k -= n
        else:
            return arr[-1] + k


s = Solution()
print(s.findKthPositive(arr = [2,3,4,7,11], k = 5))  # 9
print(s.findKthPositive(arr = [1,2,3,4], k = 2))  # 6
print(s.findKthPositive(arr = [2,3,4,7,11], k = 1000))  # 1005
print(s.findKthPositive([2], 1))