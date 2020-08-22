from math import ceil


# https://leetcode.com/problems/thousand-separator/
class Solution:

    # Runtime: 20 ms, faster than 100.00%
    def thousandSeparator(self, n: int) -> str:
        s = str(n)
        pad = ceil(len(s) / 3) * 3 - len(s)
        s = ' ' * pad + s
        return '.'.join([s[i:i+3]for i in range(0, len(s), 3)]).lstrip()


s = Solution()
print(s.thousandSeparator("987"))  # 987
print(s.thousandSeparator("1234"))  # 1.234
print(s.thousandSeparator("123456789"))  # "123.456.789"
print(s.thousandSeparator("0"))  # "0"