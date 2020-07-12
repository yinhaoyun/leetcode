class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # print(s)
        max_len, cur_len = 0, 0
        vowels = "aeiou"
        for c in s[:k]:
            if c in vowels:
                cur_len += 1
        if cur_len == k:
            return k
        max_len = cur_len
        for i in range(1, len(s) - k + 1):
            # print(s[i: i + k])
            if s[i-1] in vowels:
                cur_len -= 1
            if s[i + k - 1] in vowels:
                cur_len += 1
            max_len = max(max_len, cur_len)
        return max_len



s = Solution()
print(s.maxVowels(s="abciiidef", k=3))  # 3
print(s.maxVowels(s="aeiou", k=2))  # 2
print(s.maxVowels(s="leetcode", k=3))  # 2
print(s.maxVowels(s="rhythms", k=4))  # 0
print(s.maxVowels(s="tryhard", k=4))  # 1
print(s.maxVowels("abciiidef", 3))  # 3
print(s.maxVowels("weallloveyou", 7))  # 4