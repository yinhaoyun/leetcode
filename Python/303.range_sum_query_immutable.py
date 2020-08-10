import itertools
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sums = list(itertools.accumulate(nums))


    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.prefix_sums[j]
        return self.prefix_sums[j] - self.prefix_sums[i - 1]


if __name__ == '__main__':
    s = NumArray([-2, 0, 3, -5, 2, -1])
    print(s.sumRange(0, 2))  # 1
    print(s.sumRange(2, 5))  # -1
    print(s.sumRange(0, 5))  # -3
