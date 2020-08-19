# https://leetcode.com/problems/goat-latin/
class Solution:
    def toGoatLatin(self, S: str) -> str:
        return ' '.join([f"{s if s[0].lower() in 'aeiou' else (s[1:] + s[0])}ma{'a' * (i+1)}" for i, s in enumerate(S.split())])


if __name__ == '__main__':
    s = Solution()
    print(s.toGoatLatin("I speak Goat Latin"))  # "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
    print(s.toGoatLatin("The quick brown fox jumped over the lazy dog"))  # "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"