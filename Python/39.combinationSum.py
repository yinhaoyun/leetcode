from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combs = []

        def helper(n: int, comb: List, cur_sum: int):
            if cur_sum == target:
                combs.append(comb)
                return
            for i in range(n, len(candidates)):
                if cur_sum + candidates[i] <= target:
                    helper(i, comb + [candidates[i]], cur_sum + candidates[i])

        helper(0, [], 0)
        return combs


s = Solution()
print(s.combinationSum(candidates=[2, 3, 6, 7], target=7))
print(s.combinationSum(candidates=[2, 3, 5], target=8))
