from typing import List


class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        # http://www.noteanddata.com/leetcode-932-Beautiful-Array-java-solution-note.html
        l = [1]
        while len(l) < N:
            next_l = []
            for v in l:
                if 2*v-1 <= N:
                    next_l.append(2 * v - 1)
            for v in l:
                if 2*v <= N:
                    next_l.append(2 * v)
            l = next_l

        return l[:N]


s = Solution()
print(s.beautifulArray(1))
print(s.beautifulArray(2))
print(s.beautifulArray(3))
print(s.beautifulArray(4))
print(s.beautifulArray(5))
print(s.beautifulArray(6))
print(s.beautifulArray(7))
print(s.beautifulArray(8))