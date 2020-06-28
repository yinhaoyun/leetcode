from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return ""
        letter_map = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        combs = []

        def helper(n: int, comb: str):
            if n == len(digits):
                combs.append(comb)
                return
            for c in letter_map[int(digits[n]) - 2]:
                helper(n + 1, comb + c)

        helper(0, '')
        return combs


s = Solution()
print(s.letterCombinations("23"))
