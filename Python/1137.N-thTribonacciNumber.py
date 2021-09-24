class Solution:
    def tribonacci(self, n: int) -> int:
        t = [0, 1, 1]
        if n <= 2: return t[n]

        for i in range(2, n):
            t[0], t[1], t[2] = t[1], t[2], sum(t)
        return t[-1]