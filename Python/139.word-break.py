from functools import lru_cache
from typing import List


class Solution:
    def __init__(self):
        self.wordBreak = self.word_break_dp_dict

    @staticmethod
    def filter_word_dict(s: str, word_dict: List[str]) -> List[str]:
        return [e for e in word_dict if e in s]

    def word_break_dp_dict(self, s: str, word_dict: List[str]) -> bool:
        word_dict = Solution.filter_word_dict(s, word_dict)
        if len(word_dict) == 0:
            return False

        dp = dict()

        def helper(s: str) -> bool:
            if s in dp:
                return dp[s]
            if len(s) == 0:
                return True
            for word in word_dict:
                if s.startswith(word):
                    remain_str = s[len(word):]
                    dp[remain_str] = helper(remain_str)
                    if dp[remain_str]:
                        return True
            dp[s] = False
            return False

        return helper(s)

    def word_break_dp(self, s: str, word_dict: List[str]) -> bool:
        word_dict = Solution.filter_word_dict(s, word_dict)
        if len(word_dict) == 0:
            return False

        @lru_cache
        def helper(s: str) -> bool:
            if len(s) == 0:
                return True
            for word in word_dict:
                if s.startswith(word) and helper(s[len(word):]):
                    return True
            return False

        return helper(s)

    def word_break_recursive(self, s: str, word_dict: List[str]) -> bool:
        if s in word_dict:
            return True
        for i in range(1, len(s)):
            if s[:i] in word_dict and self.wordBreak(s[i:], word_dict):
                return True
        return False




s = Solution()
print(s.wordBreak(s="leetcode", word_dict=["leet", "code"]))  # true
print(s.wordBreak(s="applepenapple", word_dict=["apple", "pen"]))  # true
print(s.wordBreak(s="catsandog", word_dict=["cats", "dog", "sand", "and", "cat"]))  # false
print(s.wordBreak(s="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", word_dict=["a", "aa", "aaa", "aaaa", "aaaaa"]))  # false
