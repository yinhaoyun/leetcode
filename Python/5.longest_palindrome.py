import collections


class Solution:
    def longestPalindrome(self, s: str) -> str:
        return len(s) - ((len(odds) - 1) if len(odds := [c % 2 for c in collections.Counter(s).values() if c % 2]) else 0)



if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("abccccdd"))  # 7
    print(s.longestPalindrome("dd"))  # 2
    print(s.longestPalindrome("dda"))  # 3