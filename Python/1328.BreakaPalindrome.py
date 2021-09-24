class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        N = len(palindrome)
        if N <= 1: return ""

        for i in range(N//2):
            if palindrome[i] != "a":
                return palindrome[:i] + "a" + palindrome[i+1:]
        return palindrome[:-1] + "b"


if __name__ == "__main__":
    s = Solution()
    print(s.breakPalindrome("abccba")) # "aaccba"
    print(s.breakPalindrome("a")) # ""
    print(s.breakPalindrome("aa")) # ab
    print(s.breakPalindrome("aba")) # abb