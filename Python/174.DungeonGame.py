import math
import itertools
from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        CY, CX = len(dungeon), len(dungeon[0])
        dp = [[math.inf] * (CX + 1) for _ in range(CY + 1)]
        dp[-1][-2] = dp[-2][-1] = 1

        for y, x in itertools.product(range(CY - 1, -1, -1), range(CX - 1, -1, -1)):
            dp[y][x] = min(dp[y + 1][x], dp[y][x + 1]) - dungeon[y][x]
            if dp[y][x] <= 0: dp[y][x] = 1
        return dp[0][0]