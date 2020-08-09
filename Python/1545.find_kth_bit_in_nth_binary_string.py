import math
from functools import lru_cache


class Solution:
    """
    https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/
    Given two positive integers n and k, the binary string  Sn is formed as follows:
    S1 = "0"
    Si = Si-1 + "1" + reverse(invert(Si-1)) for i > 1

    S1 = "0"
    S2 = "011"
    S3 = "0111001"
    S4 = "011100110110001"
    """
    def __init__(self):
        self.findKthBit = self.bottom_up

    def divide_n_conquer(self, n, k):
        # https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/discuss/781062/Python3-4-line-divide-and-conquer
        if k == 1: return "0"
        if k == 2 ** (n - 1): return "1"
        if k < 2 ** (n - 1): return self.findKthBit(n - 1, k)
        return "0" if self.findKthBit(n - 1, 2 ** n - k) == "1" else "1"

    def bottom_up(self, n: int, k: int) -> str:
        if k == 1:
            # print("fast trick")
            return "0"
        if Solution.is_power_of_2(k): # 2, 4, 8, 16...power of 2
            # print("fast trick")
            return "1"
        binary = "0"
        while k > len(binary):
            binary = f"{binary}1{Solution.invert_n_reverse(binary)}"
        # print(results)
        return binary[k-1]

    def recursive_dp(self, n: int, k: int) -> str:
        @lru_cache
        def helper(n: int) -> str:
            if n == 1:
                return "0"
            return helper(n-1) + "1" + Solution.invert_n_reverse(helper(n-1))
        return helper(n)[k-1]

    @staticmethod
    def invert_n_reverse(s: str) -> str:
        return ''.join(["0" if c == "1" else "1" for c in s[::-1]])

    @staticmethod
    def is_power_of_2(k: int) -> bool:
        return math.log2(k).is_integer()


if __name__ == '__main__':
    s = Solution()
    print(s.findKthBit(n = 3, k = 1))  # "0"
    print(s.findKthBit(n = 4, k = 11))  # "1"
    print(s.findKthBit(n = 1, k = 1))  # "0"
    print(s.findKthBit(n = 2, k = 3))  # "1"
    print(s.findKthBit(3, 2))  # 1
    print(s.findKthBit(999, 9999))  # 1
