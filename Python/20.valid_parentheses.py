class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        pair = {'}':'{', ']':'[', ')':'('}
        for c in s:
            if c in "{[(":
                stk.append(c)
            elif stk and pair[c] == stk[-1]:
                stk.pop()
            else:
                return False
        return len(stk) == 0


if __name__ == '__main__':
    s = Solution()
    print(s.isValid("()"))  # True
    print(s.isValid("()[]{}"))
    print(s.isValid("{[]}"))
    print(s.isValid("(]"))  # False
    print(s.isValid("([)]"))
    print(s.isValid(')))'))