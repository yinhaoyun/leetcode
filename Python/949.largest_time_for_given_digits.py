import itertools
from typing import List


# https://leetcode.com/problems/largest-time-for-given-digits/949. Largest Time for Given Digits
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        largest_time = -1
        result = None
        for p in itertools.permutations(A):
            hour, minute = p[0] * 10 + p[1], p[2] * 10 + p[3]
            if hour >= 24 or minute >= 60:
                continue
            if hour * 60 + minute > largest_time:
                largest_time = hour * 60 + minute
                result = p
        if result:
            hour, minute = result[0] * 10 + result[1], result[2] * 10 + result[3]
            return "%02d:%02d" % (hour, minute)
        else:
            return ""


if __name__ == "__main__":
    s = Solution()
    print(s.largestTimeFromDigits([1,2,3,4]))  # "23:41"
    print(s.largestTimeFromDigits([5,5,5,5]))  # ""
    print(s.largestTimeFromDigits([0,0,0,0]))  # "00:00"