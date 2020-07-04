class Solution:
    def isUgly(self, num: int) -> bool:
        if num > 1:
            for i in 2,3,5:
                while num % i == 0:
                    num //= i
        return num == 1


s = Solution()
print(s.isUgly(6))  # true
print(s.isUgly(8))  # true
print(s.isUgly(1))  # true
print(s.isUgly(2))  # true
print(s.isUgly(5))  # true
print(s.isUgly(3))  # true
print(s.isUgly(14))  # false
print(s.isUgly(7))  # false

