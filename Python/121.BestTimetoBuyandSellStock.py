import math
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = math.inf
        max_profit = 0
        for p in prices:
            if p < mini:
                mini = p
            elif p - mini > max_profit:
                max_profit = p - mini
        return max_profit
