# https://leetcode.com/problems/repeated-substring-pattern/
class Solution:
    def __init__(self):
        self.repeatedSubstringPattern = self.my_solution

    def simple(self, s: str) -> bool:
        for i in range(1, len(s) // 2 + 1):
            if s[:i] * (len(s) // i) == s:
                return True
        return False

    def my_solution(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        N = len(s)
        # print(f"str={s}, N={N}")

        def helper() -> bool:
            expected_dup = N // step
            # print(f"step={step}, expected_dup={expected_dup}")
            for start in range(step):
                step_chars = [c for c in s[start::step] if c == s[start]]
                # print(f"start={start}, step_chars={step_chars}")
                if len(step_chars) != expected_dup:
                    return False
            return True

        for step in [n for n in range(1, N // 2 + 1) if N % n == 0]:
            if helper():
                return True
        return False



if __name__ == "__main__":
    s = Solution()
    print(s.repeatedSubstringPattern("aa"))  # True
    print(s.repeatedSubstringPattern("abab"))  # True
    print(s.repeatedSubstringPattern("abcabc"))  # True
    print(s.repeatedSubstringPattern("abcabcabc"))  # True
    print(s.repeatedSubstringPattern("abcabcabcabc"))  # True
    print(s.repeatedSubstringPattern("abcabcabcabcabc"))  # True
    print(s.repeatedSubstringPattern("abcabcabcabcabcabc"))  # True
    print(s.repeatedSubstringPattern("abaababaab"))  # True
    print()
    print(s.repeatedSubstringPattern("abcabcabcabcabcaba"))  # False
    print(s.repeatedSubstringPattern("aba"))  # False
    print(s.repeatedSubstringPattern("a"))  # False
    print(s.repeatedSubstringPattern(""))  # False
