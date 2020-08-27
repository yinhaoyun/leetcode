import bisect
from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]):
        ints = sorted([[j, k, i] for i, (j, k) in enumerate(intervals)])
        begs = [i for i, _, _ in ints]
        result = [-1] * len(intervals)
        for i, j, k in ints:
            t = bisect.bisect_left(begs, j)
            if t < len(begs):
                result[k] = ints[t][2]

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.findRightInterval([[1, 2]]))  # [-1]
    print(s.findRightInterval([[3, 4], [2, 3], [1, 2]]))  # [-1, 0, 1]
    print(s.findRightInterval([[1, 4], [2, 3], [3, 4]]))  # [-1, 2, -1]
