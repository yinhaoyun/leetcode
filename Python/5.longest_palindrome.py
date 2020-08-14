import collections


class Solution:
    def longestPalindrome(self, s: str) -> str:
        counts = collections.Counter(s)
        odds = [c % 2 for c in counts.values() if c % 2]
        return len(s) - ((len(odds) - 1) if len(odds) else 0)



if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("abccccdd"))  # 7
    print(s.longestPalindrome("dd"))  # 2
    print(s.longestPalindrome("dda"))  # 3