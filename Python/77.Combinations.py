from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        comb = []

        def backtrack(curr=1) -> None:
            nonlocal ans, comb
            if len(comb) == k:
                ans.append(list(comb))
                return
            for i in range(curr, n + 1):
                if n + 1 - i < k - len(comb): # Pruning
                    break
                comb.append(i)
                backtrack(i + 1)
                comb.pop()

        backtrack()
        return ans


s = Solution()
print(s.combine(n=4, k=2))
print(s.combine(n=1, k=1))
print(s.combine(n=3, k=3))
