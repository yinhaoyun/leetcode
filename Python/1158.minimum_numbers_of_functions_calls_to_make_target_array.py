from math import log2, log
from typing import List


# https://leetcode.com/problems/minimum-numbers-of-function-calls-to-make-target-array/
class Solution:

    # brilliant: https://leetcode.com/problems/minimum-numbers-of-function-calls-to-make-target-array/discuss/805740/JavaC%2B%2BPython-Bit-Counts
    # Runtime: 316 ms, faster than 100.00%
    def minOperations(self, nums: List[int]) -> int:
        op0 = sum(bin(n).count("1") for n in nums)
        op1 = len(bin(max(nums))) - 3
        return op0 + op1

    # Runtime: 3084 ms, faster than 25.00%
    def my_solution(self, nums: List[int]) -> int:
        ops = 0

        def op0() -> int:
            nonlocal nums
            ops = sum([n % 2 for n in nums])
            nums = [((n >> 1) << 1) for n in nums]
            return ops

        def op1() -> int:
            nonlocal nums
            ops = 0
            while sum([n % 2 for n in nums]) == 0:
                ops += 1
                nums = [n // 2 for n in nums]
            return ops

        # print(nums)
        while sum(nums):
            ops += op0()
            # print(f"op0: {nums}, ops={ops}")
            if sum(nums):
                ops += op1()
                # print(f"op1: {nums}, ops={ops}")

        return ops


s = Solution()
print(s.minOperations([1,5]))  # 5
print(s.minOperations([2,2]))  # 3
print(s.minOperations([4,2,5]))  # 6
print(s.minOperations([3,2,2,4]))  # 7
print(s.minOperations([2,4,8,16]))  # 8
print(s.minOperations([1000000000]))