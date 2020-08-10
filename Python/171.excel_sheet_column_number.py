class Solution:
    """
    https://leetcode.com/problems/excel-sheet-column-number/
    """
    def __init__(self):
        self.titleToNumber = self.list_comp

    def list_comp(self, s: str) -> int:
        return sum([(ord(c) - ord("A") + 1) * 26**i for i, c in enumerate(s[::-1])])

    def loop_multiple(self, s: str) -> int:
        def number(c: str) -> int:
            return ord(c) - ord("A") + 1
        res = 0
        for c in s:
            res = res * 26 + number(c)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.titleToNumber('A'))  # 1
    print(s.titleToNumber('AA'))  # 27
    print(s.titleToNumber('AB'))  # 28
    print(s.titleToNumber('ZY'))  # 701