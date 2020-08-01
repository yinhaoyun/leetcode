from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)  # n steps
        if n <= 1:
            return 0
        dp = [-1] * (n + 1)
        dp[0] = 0
        dp[1] = 0

        def helper(l: int):
            if dp[l] == -1:
                dp[l] = min(helper(l-1) + cost[l-1], helper(l-2) + cost[l-2])
            return dp[l]
        return helper(n)

s = Solution()
print(s.minCostClimbingStairs([10, 15, 20]))  # 15
print(s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))  # 6
print(s.minCostClimbingStairs([10]))  # 15
print(s.minCostClimbingStairs([1, 100]))  # 6