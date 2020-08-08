from functools import lru_cache


class Solution:
    def __init__(self):
        self.minAddToMakeValid = self.count_open_close

    # Standard
    def stack(self, s: str) -> int:
        stk = []
        for c in s:
            if c == "(":
                stk.append(c)
            else:
                if stk and stk[-1] == "(":
                    stk.pop()
                else:
                    stk.append(c)
        return len(stk)

    # Smarter
    def count_open_close(self, s: str) -> int:
        open, close = 0, 0
        for c in s:
            if c == "(":
                open += 1
            else:
                if open > 0:
                    open -= 1;
                else:
                    close += 1
        return open + close


    # TLE
    def divide_n_conquer_resursive(self, s: str) -> int:
        # print(s)
        @lru_cache
        def helper(s: str) -> int:
            while s.count("()"):
                s = s.replace("()", "")
            print(s)
            if len(s) <= 1:
                return len(s)
            result = []
            for i in range(1, len(s)):
                result += [helper(s[:i]) + helper(s[i:])]
            return min(result)
        return helper(s)


if __name__ == '__main__':
    s = Solution()
    print(s.minAddToMakeValid("())"))  # 1
    print(s.minAddToMakeValid("((("))  # 3
    print(s.minAddToMakeValid("()"))  # 0
    print(s.minAddToMakeValid("))()()(()))(()))()((()((()()))))))())))))()()))(()()(())))))(()())(((()()))())))(()))()(((()((())((()()())())()((()))(()))(())))))()()()(())))))(()()()(())(()())(()))))(()((()(()(()()))(((((()()((())"))  # 35