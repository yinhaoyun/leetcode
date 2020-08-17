from typing import List


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        left, right = [0] * n, [0] * n

        min_left = prices[0]
        for i in range(1, n):
            left[i] = max(left[i-1], prices[i] - min_left)
            min_left = min(min_left, prices[i])

        max_right = prices[-1]
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], max_right - prices[i])
            max_right = max(max_right, prices[i])

        return max([l + r for (l, r) in zip(left, right)])


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([3,3,5,0,0,3,1,4]))  # 6
    print(s.maxProfit([1,2,3,4,5]))  # 4
    print(s.maxProfit([7,6,4,3,1]))  # 0

