from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combs = []
        comb=''
        l=r=n
        def helper(comb, l, r):
            if l == 0 and r == 0:
                combs.append(comb)
                return
            if l != 0:
                helper(comb + '(', l - 1, r)
            if r > l:
                helper(comb + ')', l, r - 1)


        helper(comb, n, n)
        return combs

s = Solution();
print(s.generateParenthesis(3))