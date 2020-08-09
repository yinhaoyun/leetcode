
class Solution:
    """
    https://leetcode.com/contest/weekly-contest-201/problems/make-the-string-great/
    https://leetcode.com/problems/make-the-string-great/
    """
    CASE_DIFF = abs(ord("a") - ord("A"))

    def __init__(self):
        self.makeGood = self.stack

    def stack(self, s: str) -> str:
        stk = []
        for c in s:
            if stk and Solution.bad(stk[-1], c):
                stk.pop()
            else:
                stk.append(c)

        return ''.join(stk)

    @staticmethod
    def bad(c1: str, c2: str):
        return abs(ord(c1) - ord(c2)) == Solution.CASE_DIFF

    def loop_check_diff(self, s: str) -> str:
        if len(s) < 2:
            return s

        while True:
            asciis_diff = [abs(ord(c1) - ord(c2)) for c1, c2 in zip(s[:-1], s[1:])]
            try:
                del_index = asciis_diff.index(Solution.CASE_DIFF)
                s = s[:del_index] + s[del_index + 2:]
            except ValueError:
                break
        return s


if __name__ == '__main__':
    s = Solution()
    print(s.makeGood("leEeetcode"))  # "leetcode"
    print(s.makeGood("abBAcC"))  # ""
    print(s.makeGood("s"))  # s
