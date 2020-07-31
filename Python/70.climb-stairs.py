class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp_1 = 1
        dp_2 = 2

        for i in range(3, n + 1):
            dp_2, dp_1 = dp_1 + dp_2, dp_2
        return dp_2


s = Solution()
for i in range(10):
    print(i, s.climbStairs(i))