from functools import lru_cache
from typing import List
import math


# https://leetcode.com/problems/minimum-cost-for-tickets/
class Solution:

    # TODO: write by myself
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @lru_cache(None)
        def helper(day) -> int:
            if day >= len(days):
                return 0
            day_pass = [0] * len(costs)
            day_pass[0] = helper(day + 1) + costs[0]

            i = 0
            while i < len(days):
                if days[i] >= days[day] + 7:
                    break
                i += 1
            day_pass[1] = helper(i) + costs[1]

            while i < len(days):
                if days[i] >= days[day] + 30:
                    break
                i += 1
            day_pass[2] = helper(i) + costs[2]
            return min(day_pass)


        return helper(0)

if __name__ == "__main__":
    s = Solution()
    print(s.mincostTickets(days = [1,4,6,7,8,20], costs = [2,7,15]))  # 11
    print(s.mincostTickets(days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]))  # 17

