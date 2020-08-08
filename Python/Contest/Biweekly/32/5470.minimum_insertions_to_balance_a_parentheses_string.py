from functools import lru_cache

"""
https://leetcode.com/contest/biweekly-contest-32/problems/minimum-insertions-to-balance-a-parentheses-string/
FIXME
"""
class Solution:
    def minInsertions(self, s: str) -> int:
        @lru_cache
        def helper(part: str) -> int:
            new_part = part.replace("())", "")
            if new_part == "())":
                return 0
            if new_part in ("()", "))"):
                return 1
            if new_part in ("(", ")"):
                return 2
            insert_count = []
            for i in range(1, len(new_part)):
                insert_count.append(helper(new_part[:i]) + helper(new_part[i:]))
            return min(insert_count)
        return helper(s)


s = Solution()
print(s.minInsertions("(()))"))  # 1: (())))
print(s.minInsertions("())"))  # 0
print(s.minInsertions("))())("))  # 3: "())())())"
print(s.minInsertions("(((((("))  # 12: "(((((())))))))))))"
print(s.minInsertions(")))))))"))  # 5: "(((())))))))"