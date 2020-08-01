class Solution:
    def __init__(self):
        self.detectCapitalUse = self.my_func

    def python_func(self, word: str) -> bool:
        return word.upper() == word or word.capitalize() == word or word.lower() == word


s = Solution()
print(s.detectCapitalUse("leetcode"))  # True
print(s.detectCapitalUse("USA"))  # True
print(s.detectCapitalUse("Google"))  # True
print(s.detectCapitalUse("uSA"))  # False
print(s.detectCapitalUse("leetCode"))  # False
print(s.detectCapitalUse("GoogleApple"))  # False
