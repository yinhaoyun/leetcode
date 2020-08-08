import math


class Solution:
    def __init__(self):
        self.isPowerOfThree = self.log

    def log(self, n: int) -> bool:
        if n < 1:
            return False
        power = round(math.log(n, 3))
        return 3**power == n

    def loop(self, n: int) -> bool:
        if n == 0:
            return False
        while n != 1:
            if n % 3:
                return False
            n = n // 3
        return True


if __name__ == '__main__':
    s = Solution()
    for i in range(0, 28):
        # print(i, bin(i))
        print(s.isPowerOfThree(i))
    print(s.isPowerOfThree(243))