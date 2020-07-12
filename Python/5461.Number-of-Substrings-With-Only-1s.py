class Solution:
    def numSub(self, s: str) -> int:
        res = 0
        prev_is_1 = False
        cont_count = 0

        def helper(n: int):
            return (1 + n) * n / 2


        s = s + "0"
        for c in s:
            if c == "1":
                cont_count += 1
            else:
                res += helper(cont_count)
                cont_count = 0



        return int(res % (10**9+7))

s = Solution()
print(s.numSub("0110111"))  # 9
print(s.numSub("101"))  # 2
print(s.numSub("111111"))  # 21
