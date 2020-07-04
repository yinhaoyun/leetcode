from math import sqrt


class Solution:
    def arrangeCoins(self, n: int) -> int:
        # print(n)
        def f(k: int) -> int:
            return int((1 + k) * k / 2)

        x = int(sqrt(2*n))
        # print("x=", x, ", f(x)=", f(x))
        while f(x) > n:
            x -= 1
            # print("x=", x, ", f(x)=", f(x))
        return x


s = Solution()
print(s.arrangeCoins(5))  # 2
print(s.arrangeCoins(6))  # 3
print(s.arrangeCoins(7))  # 3
print(s.arrangeCoins(8))  # 3
print(s.arrangeCoins(9))  # 3
print(s.arrangeCoins(10))  # 4
print(s.arrangeCoins(11))  # 4
print(s.arrangeCoins(12))  # 4
