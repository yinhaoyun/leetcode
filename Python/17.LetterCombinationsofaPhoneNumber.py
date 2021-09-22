from typing import List


class Solution:
    LETTERS = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

    def letterCombinations(self, digits: str) -> List[str]:
        if not len(digits): return []
        ans = []

        def helper(result: str) -> None:
            if len(result) == len(digits):
                ans.append(result)
                return
            for c in Solution.LETTERS[int(digits[len(result)])]:
                helper(result + c)

        helper("")
        return ans


    def letterCombinations_bfs(self, digits: str) -> List[str]:
        if not len(digits): return []
        ans = [""]

        for d in digits:
            tmp = []
            for a in ans:
                for c in Solution.LETTERS[int(d)]:
                    tmp.append(a + c)
            ans = tmp

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.letterCombinations("23"))
    print(s.letterCombinations(""))
    print(s.letterCombinations("2"))