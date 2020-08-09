from functools import lru_cache
from math import inf
from typing import List, Tuple


class Solution:
    """
    https://leetcode.com/problems/minimum-cost-to-cut-a-stick/
    https://leetcode.com/contest/weekly-contest-201/problems/minimum-cost-to-cut-a-stick/
    """

    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        print(cuts)

        @lru_cache(maxsize=None)
        def helper(n: int, cuts: Tuple[int]) -> int:
            if len(cuts) == 0:
                return 0
            if len(cuts) == 1:
                return n
            mini = inf
            # print("cuts", cuts, len(cuts))
            for i, c in enumerate(cuts):
                cuts1 = cuts[:i]
                cuts2 = [cut - c for cut in cuts[i+1:]]
                # print("loop", i, cuts1, c, cuts2)
                cur_cost = helper(c, cuts1) + helper(n-c, tuple(cuts2))
                if cur_cost < mini:
                    mini = cur_cost
            else:
                pass
                # print(helper.cache_info())
                # print("end loop", i, c)
            return mini + n
        return helper(n, tuple(cuts))


if __name__ == '__main__':
    s = Solution()
    print(s.minCost(n = 7, cuts = [1,3,4,5]))  # 16
    print(s.minCost(n = 9, cuts = [5,6,1,4,2]))  # 22
    print(s.minCost(30, [13,25,16,20,26,5,27,8,23,14,6,15,21,24,29,1,19,9,3]))  # TLE
    print(s.minCost(43, list(range(1,43))))  # TLE
    print(s.minCost(43, [19,24,11,18,16,34,27,38,26,12,40,36,28,14,15,41,33,20,2,21,13,5,42,23,30,32,8,37,10]))  # TLE
    print(s.minCost(83, [40,23,68,45,31,77,69,71,36,13,12,49,35,60,67,58,28,61,66,29,80,57,1,8,39,73,18,7,59,44,65,30,15,43,21,55,19,16,38,72,14,9,51,48,34,33,79,20,74,56,52,42,3,4,54,75,62,46,41,10,50,25,47]))  # TLE