class Solution:
    def isPalindrome(self, s: str) -> bool:
        ALPHA = 'abcdefghijklmnopqrstuvwxyz1234567890'
        s = ''.join([c for c in s.lower() if c in ALPHA])
        return s == s[::-1]