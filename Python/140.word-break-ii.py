from collections import defaultdict
from functools import lru_cache
from typing import List, Set


class Solution:
    def __init__(self):
        self.wordBreak = self.word_break_someone

    @staticmethod
    def filter_word_dict(s: str, word_dict: List[str]) -> Set[str]:
        return set([e for e in word_dict if e in s])

    # TODO: Complete my solution
    def word_break_dp(self, s: str, word_dict: List[str]) -> List[str]:
        word_set = Solution.filter_word_dict(s, word_dict)

        if len(word_set) == 0:
            return []

        def helper(s: str, formed: List[str]) -> bool:
            if dp.get(s) is not None:
                formed.append(dp_formed[s])
                ret.append(" ".join(formed))
                return dp[s]
            if s in word_set:
                formed.append(s)
                ret.append(" ".join(formed))
                return True

            for word in word_set:
                if s.startswith(word) and helper(s[len(word):], formed + [word]):
                    pass

        ret = []
        dp = dict()
        dp_formed = dict()
        helper(s, [])
        return ret

    def word_break_recursive(self, s: str, word_dict: List[str]) -> List[str]:
        word_set = Solution.filter_word_dict(s, word_dict)

        if len(word_set) == 0:
            return []

        def helper(s: str, formed: List[str]) -> None:
            if s in word_set:
                formed.append(s)
                ret.append(" ".join(formed))
                return

            for word in word_set:
                if s.startswith(word) and helper(s[len(word):], formed + [word]):
                    pass

        ret = []
        helper(s, [])
        return ret

    # https://leetcode.com/problems/word-break-ii/discuss/763803/Python-Simple-DP-Solution
    def word_break_someone(self, s: str, word_dict: List[str]) -> List[str]:
        dp = defaultdict(list)

        def helper(start: int) -> List[str]:
            if start not in dp:
                for w in word_dict:
                    if start + len(w) <= len(s) and w == s[start:start + len(w)]:
                        if start + len(w) == len(s):
                            # Case 1: No need to go deeper because we are at the end of s
                            dp[start].append(w)
                        else:
                            # Case 2: Keep searching deeper
                            for suffix in helper(start + len(w)):
                                dp[start].append(w + " " + suffix)
            return dp[start]

        return helper(0)


s = Solution()
print(s.wordBreak(s="catsanddog", word_dict=["cat", "cats", "and", "sand", "dog"]))  # ["cats and dog", "cat sand dog" ]
print(s.wordBreak(s="pineapplepenapple", word_dict=["apple", "pen", "applepen", "pine", "pineapple"]))
'''
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
'''
print(s.wordBreak(s="catsandog", word_dict=["cats", "dog", "sand", "and", "cat"]))  # []
print(
    s.wordBreak(s="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
                word_dict=["a", "aa", "aaa", "aaaa", "aaaaa"]))  # false
