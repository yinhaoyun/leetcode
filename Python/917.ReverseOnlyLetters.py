class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s2 = [c for c in s]
        i, j = -1, len(s2)

        def advanceIJ() -> bool:
            nonlocal i, j
            i, j = i + 1, j - 1
            if i >= j:
                return False
            while not s2[i].isalpha():
                if i + 1 < j:
                    i += 1
                else:
                    return False
            while not s2[j].isalpha():
                if i < j - 1:
                    j -= 1
                else:
                    return False
            return i < j

        while advanceIJ():
            s2[i], s2[j] = s2[j], s2[i]

        return "".join(s2)


if __name__ == "__main__":
    s = Solution()
    print(s.reverseOnlyLetters("ab-cd")) # Output: "dc-ba"
    print(s.reverseOnlyLetters("a-bC-dEf-ghIj")) # Output: "j-Ih-gfE-dCba"
    print(s.reverseOnlyLetters("Test1ng-Leet=code-Q!")) # Output: "Qedo1ct-eeLg=ntse-T!"
    print(s.reverseOnlyLetters("7_28]")) #
