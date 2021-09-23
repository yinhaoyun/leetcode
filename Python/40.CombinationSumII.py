from typing import List
from collections import Counter

class Solution:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []

        def backtrack(comb: List, remain: int, curr: int, counter: List, results: List):
            if remain == 0:
                results.append(list(comb))
                return

            for next_curr in range(curr, len(counter)):
                cand, freq = counter[next_curr]

                if freq <= 0:
                    continue
                if remain - cand >= 0:
                    comb.append(cand)
                    counter[next_curr] = (cand, freq - 1)

                    backtrack(comb, remain - cand, next_curr, counter, results)

                    counter[next_curr] = (cand, freq)
                    comb.pop()

        counter = Counter(candidates)
        counter = [(c, counter[c]) for c in counter]
        backtrack(comb = [], remain = target, curr = 0, counter = counter, results = results)
        return results

    def combinationSum2_dfs(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = set()
        path = []

        def dfs(index: int, target: int) -> None:
            if target == 0:
                ans.add(tuple(path))
                return

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                cand = candidates[i]
                if target - cand >= 0:
                    path.append(cand)
                    dfs(i + 1, target - cand)
                    path.pop()

        dfs(0, target)
        return [list(t) for t in ans]


if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8))  # [1,1,6], [1,2,5], [1,7], [2,6]
    print(s.combinationSum2_dfs(candidates=[10, 1, 2, 7, 6, 1, 5], target=8))  # [1,1,6], [1,2,5], [1,7], [2,6]
    print(s.combinationSum2(candidates=[2, 5, 2, 1, 2], target=5))  # [1,2,2], [5]
    print(s.combinationSum2_dfs(candidates=[2, 5, 2, 1, 2], target=5))  # [1,2,2], [5]
    print(s.combinationSum2([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 27))  # []
    print(s.combinationSum2_dfs([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 27))  # []
