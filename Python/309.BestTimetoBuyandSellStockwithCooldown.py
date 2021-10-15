from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        hold, sold, cd = -prices[0], 0, 0

        for i in range(1, N):
            hold, sold, cd = \
                max(hold, cd - prices[i]), \
                prices[i] + hold, \
                max(cd, sold)
        return max(sold, cd)


    def maxProfit_readable(self, prices: List[int]) -> int:
        N = len(prices)
        hold = -prices[0]
        sold = 0
        cd = 0

        for i in range(1, N):
            hold += max(hold[i - 1], cd[i - 1] - prices[i]),
            sold += prices[i] + hold[i - 1],
            cd += max(cd[i - 1], sold[i - 1]),

        return max(cd[-1], sold[-1])


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([1, 2, 3, 0, 2]))  # 3
    print(s.maxProfit([1]))  # 0
