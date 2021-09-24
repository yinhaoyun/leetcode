from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = [s]
        for i, c in enumerate(s):
            if c.isalpha():
                ans += [a[:i] + c.swapcase() + a[i + 1:] for a in ans]
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.letterCasePermutation("a1b2")) # ["a1b2","a1B2","A1b2","A1B2"]
    print(s.letterCasePermutation("3z4")) # ["3z4","3Z4"]
    print(s.letterCasePermutation("12345")) # "12345"
    print(s.letterCasePermutation("0")) # 0