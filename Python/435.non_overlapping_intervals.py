import math
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        result, cur_end = 0, -math.inf
        for s, e in intervals:
            if s >= cur_end:
                cur_end = e
            else:
                result += 1
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))  # 1: [1, 3]
    print(s.eraseOverlapIntervals([[1,2],[1,2],[1,2]]))  # 2: [1, 2]
    print(s.eraseOverlapIntervals([[1,2],[2,3]]))  # 0
    print(s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7]]))  # 0