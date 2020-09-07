# https://leetcode.com/problems/word-pattern/
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        S = s.split()
        if len(pattern) != len(S):
            return False
        dic = {}
        words = set()
        for i, c in enumerate(pattern):
            if not dic.get(c):
                if S[i] in words:
                    return False
                dic[c] = S[i]
                words.add(S[i])
            elif dic[c] != S[i]:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.wordPattern("abba", "dog cat cat dog"))  # True
    print(s.wordPattern("abba", "dog cat cat fish"))  # False
    print(s.wordPattern("aaaa", "dog cat cat dog"))  # False
    print(s.wordPattern("abba", "dog dog dog dog"))  # False
