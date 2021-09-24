class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        N = len(palindrome)
        if N <= 1:
            return ""
        pld_list = list(palindrome)

        if pld_list[0] != "a":
            pld_list[0] = "a"
        else:
            for i in range(N//2):
                if pld_list[i] != "a":
                    pld_list[i] = "a"
                    break
            else:
                pld_list[N-1] = "b"
        return "".join(pld_list)

if __name__ == "__main__":
    s = Solution()
    print(s.breakPalindrome("abccba")) # "aaccba"
    print(s.breakPalindrome("a")) # ""
    print(s.breakPalindrome("aa")) # ab
    print(s.breakPalindrome("aba")) # abb