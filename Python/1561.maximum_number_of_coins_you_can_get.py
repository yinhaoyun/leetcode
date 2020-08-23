from typing import List


# https://leetcode.com/problems/maximum-number-of-coins-you-can-get/
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles) // 3
        return sum(sorted(piles)[n::2])


if __name__ == "__main__":
    s = Solution()
    print(s.maxCoins([2,4,1,2,7,8]))  # 9
    print(s.maxCoins([2,4,5]))  # 4
    print(s.maxCoins([9,8,7,6,5,1,2,3,4]))  # 18 = 8 + 6 + 4