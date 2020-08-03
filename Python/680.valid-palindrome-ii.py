class Solution:
    def validPalindrome(self, s: str) -> bool:
        # print(s)
        # print(s[::-1])
        def is_palindrom(s: str) -> bool:
            return s == s[::-1]
        head = 0
        tail = len(s) - 1
        while head < tail:
            if s[head] != s[tail]:
                if s[head + 1] == s[tail] and is_palindrom(s[head+2:tail]):
                    return True
                elif s[head] == s[tail - 1] and is_palindrom(s[head+1:tail-1]):
                    return True
                else:
                    return False
            head += 1
            tail -= 1
        return True


s = Solution()
print(s.validPalindrome("aba"))
print(s.validPalindrome("abca"))
print(s.validPalindrome("abcdezzzzzzzzzzzzzzedca"))
print(s.validPalindrome("acdezzzzzzzzzzzzzzedcba"))
print(s.validPalindrome(
    "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))  # True
print(s.validPalindrome("abcda"))  # False
print(s.validPalindrome("abcdezzzzzzzzzzzzzzedbca"))
