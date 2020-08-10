import itertools
from typing import List

# https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/
class Solution:

    def __init__(self):
        self.canThreePartsEqualSum = self.find_by_prefix_sum

    # 308 ms, faster than 99.57%
    def find_by_prefix_sum(self, A: List[int]) -> bool:
        prefix_sums = list(itertools.accumulate(A))
        if prefix_sums[-1] % 3:
            return False
        TARGET = prefix_sums[-1] // 3
        try:
            return prefix_sums.index(TARGET * 2, prefix_sums.index(TARGET) + 1) < len(prefix_sums) - 1
        except ValueError:
            return False

    # 308 ms, faster than 99.57%
    def prefix_sum_iterator(self, A: List[int]) -> bool:
        SUM_A = sum(A)
        if SUM_A % 3:
            return False
        TARGET = SUM_A // 3
        prefix_sums = itertools.accumulate(A)
        try:
            next(x for x in prefix_sums if x == TARGET)
            next(x for x in prefix_sums if x == TARGET * 2)
            return next(prefix_sums) is not None
        except StopIteration:
            return False


    # 312 ms, faster than 99.42%
    def iterate_prefix_sum(self, A: List[int]) -> bool:
        SUM_A = sum(A)
        if SUM_A % 3:
            return False
        prefix_sums = itertools.accumulate(A)
        TARGET, prev_sum , count = SUM_A // 3, 0, 0
        for i, s in enumerate(prefix_sums):
            if s - prev_sum == TARGET:
                count += 1
                if count == 2 and i < len(A) - 1:
                    return True
                prev_sum = s
        return False

    #  316 ms, faster than 98.55%
    def prefix_sum(self, A: List[int]) -> bool:
        prefix_sums = list(itertools.accumulate(A))
        # print(prefix_sums)
        if prefix_sums[-1] % 3:
            return False
        TARGET, prev_sum , count = prefix_sums[-1] // 3, 0, 0
        for i, s in enumerate(prefix_sums):
            if s - prev_sum == TARGET:
                count += 1
                if count == 2 and i < len(prefix_sums) - 1:
                    return True
                prev_sum = s
        return False

    # 324 ms, 94.50%
    def loop_count(self, A: List[int]) -> bool:
        sum_a = sum(A)
        if sum_a % 3:
            return False
        avg_a = sum_a // 3
        count = 0
        part_sum = 0
        for i, a in enumerate(A):
            part_sum += a
            if part_sum == avg_a:
                count += 1
                if count == 2 and i < len(A) - 1:
                    return True
                part_sum = 0
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1]))  # True
    print(s.canThreePartsEqualSum([3,3,6,5,-2,2,5,1,-9,4]))  # True
    print(s.canThreePartsEqualSum([12,-4,16,-5,9,-3,3,8,0]))  # True
    print(s.canThreePartsEqualSum([0,2,1,-6,6,7,9,-1,2,0,1]))  # False
    print(s.canThreePartsEqualSum([1,-1,1,-1]))  # False
